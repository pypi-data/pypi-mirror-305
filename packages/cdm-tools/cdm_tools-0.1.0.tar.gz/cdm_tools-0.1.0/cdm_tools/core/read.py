import sys
import re
import functools

from typing import Optional

from pyspark.sql import Column, DataFrame, functions as F

if sys.version_info < (3, 10):

    def pairwise(iterable):
        # pairwise('ABCDEFG') → AB BC CD DE EF FG
        iterator = iter(iterable)
        a = next(iterator, None)
        for b in iterator:
            yield a, b
            a = b
else:
    from itertools import pairwise

from cdm_tools.core.order import assign_row_number


FieldParameters = tuple[str, int, Optional[int]]


def cp_read(
    filepath: str,
    pattern: str = ".*",
    recursive: bool = False,
    fs_func: callable = None,
    read_func: callable = None,
    union_func: callable = DataFrame.unionByName,
) -> DataFrame:
    pattern = re.compile(pattern)
    files = filter(
        lambda fp: isinstance(pattern.match(fp), re.Match),
        fs_func(filepath, recursive=recursive),
    )
    return functools.reduce(union_func, map(read_func, files))


def cp_read_fwf(
    filepath: str,
    column_mapping: list | dict,
    delimiter: Optional[str] = "<><><>",
    column_extract: Optional[str] = "_c0",
    drop_extract: Optional[bool] = True,
    preserve_order: Optional[bool] = True,
    preserve_by: Optional[Column] = F.lit(1),
    read_func: Optional[callable] = None,
    union_func: Optional[callable] = None,
) -> DataFrame:
    """
    Iteratively extract data from `column_extract` using the column names and positions
    provided in the `column_mapping` sequence.

    As of v2.0, multiple sequences can be provided to dynamically read fixed width files.
    This suits data that needs to be parsed differently depending on the nature of the row

    Parameters
    ==========
    filepath: str
        Path to file. This will be passed to `read_func`.
    column_mapping: list | dict
        List of column mappings or dictionary containing group mappings. Please see example
        for more detials.
    delimiter: Optional[str]
        Delimiter of file. This should be a value that is not found in your data so that
        cp_read_fwf can force the data into one column.
    column_extract: Optional[str]
        Name of column to extract data from. By default, it is '_c0', the default name PySpark
        assigns to a DataFrame without column names.
    drop_extract: Optional[bool]
        Whether or not to remove the extract column after processing. By default, this column
        is not preserved.
    preserve_order: Optional[bool]
        Whether or not to preserve the order of the original data. By default, the order is
        preserved.
    preserve_by: Optional[Column]
        Which column(s) to preserve the order by. By default, the order is preserved by a
        dummy column to force PySpark to keep the row order the same as the original data.
    read_func: Optional[callable]
        Function to read data from `filepath`.
    union_func: Optional[callable]
        Function to union data. Currently not yet implemented.

    Returns
    =======
    DataFrame
        Data parsed out according to mappings provided.

    Raises
    ======
    AssertionException
        If mapping is not correctly defined. Please review the error message.
    AssertionException
        If the number of matched rows is less than the number of total rows.

    Example
    =======
    >>> column_mapping = [
        ("column1", 1),         # creates `column1` as substring 1:4
        ("column2", 5),         # creates `column2` as substring 5:14
        ("column3", 15),        # creates `column3` as substring 15:...
        # ... additional column-index pairs ...
        ("columnN", 100),       # creates `columnN` as substring 100:199
        ("", 200)               # column will not be created since there is no next pair
    ]

    >>> data = cp_read_fwf(filepath="path/to/fwf.txt", column_mapping=column_mapping)
    >>> # ... good idea to trim values across all columns to remove extra spaces ...
    >>> data = data.withColumns({column: F.trim(column) for column in data.columns})

    >>> # using dynamic readin
    >>> ### define all mappings
    >>> group_one_mapping = [...]
    >>> group_two_mapping = [...]
    >>> group_three_mapping = [...]
    >>> ### define all predicates
    >>> group_one_predicate = [...]
    >>> group_two_predicate = [...]
    >>> group_three_predicate = [...]
    >>> ### create mapping as grouping of mappings
    >>> column_mapping = {
        "Group One": {
            "predicate": group_one_predicate,
            "mapping": group_one_mapping
        },
        ...
    }
    >>> data = cp_read_fwf(filepath="path/to/fwf.txt", column_mapping=column_mapping)
    """

    def assert_valid_inputs(mapping: dict):
        if read_func is None:
            raise ValueError(
                "Please pass a readin-function to `read_func` (e.g. cp.read)"
            )

        ERROR_MESSAGE_TYPES = "Please revise your parameters. Each pair must be of type (str, int). See example for more details."
        assert all(
            isinstance(name, str) and all(isinstance(i, int) for i in index)
            for name, *index in mapping
        ), ERROR_MESSAGE_TYPES

        ERROR_MESSAGE_ORDER = "Please revise your column mapping. The starting index of all pairs must be in ascending order."
        assert mapping == sorted(mapping, key=lambda pair: pair[1]), ERROR_MESSAGE_ORDER

        ERROR_MESSAGE_OVERLAPPING = "Please review your column mapping. The length of a field cannot surpass the next field's starting index."
        assert all(
            start + length <= next_start
            for (_, start, length), (_, next_start, _) in pairwise(mapping)
        ), ERROR_MESSAGE_OVERLAPPING

    read_func = functools.partial(read_func, delimiter=delimiter)
    data = read_func(filepath)

    def parse_fixed_width_fields(
        data: DataFrame, column_mapping: list[FieldParameters] = column_mapping
    ) -> DataFrame:
        """Given a column mapping, parse the fixed width field into multiple fields based on column mapping."""

        def reformat_parameters(
            mapping: list[tuple[str, int, Optional[int]]],
        ) -> list[tuple[str, int, int]]:
            """Attach length if not provided in mapping."""
            return [
                (name, start, length[0] if length else end - start)
                for (name, start, *length), (_, end, *_) in pairwise(mapping)
            ]

        column_mapping = reformat_parameters(mapping=column_mapping)
        assert_valid_inputs(mapping=column_mapping)
        return data.withColumns(
            {
                column: F.trim(
                    F.substring(
                        column_extract,
                        pos=start,
                        len=length,
                    )
                )
                for (column, start, length) in column_mapping
            }
        ).drop(column_extract if drop_extract else "")

    def dynamic_readin(
        data: DataFrame,
        column_mapping: dict[str, dict] = column_mapping,
    ) -> DataFrame:
        """If given multiple mappings, format the mappings in an iterable structure to allow proper parsing."""

        def assert_groups(groups: dict) -> None:
            """Ensure mapping groups capture the entirety of the data provided."""
            group_count = 0
            for group, parameters in groups.items():
                data_count = parameters.get("data").count()
                group_count += data_count
                print(f"Group: {group:<30} | Matched rows: {data_count:,}")

            data_count = data.count()
            assert group_count == data_count, f"""
                [WARNING] Given {data_count:,} rows, the groups can only parse {group_count:,} ({abs(data_count - group_count) / data_count:.1%}) rows.
                Please revise your mapping.
                """

        def bucket_groups(
            data: DataFrame = data, mapping: dict = column_mapping
        ) -> dict:
            """Split data into groups given predicates in the mapping"""
            if preserve_order:
                data = assign_row_number(data=data, preserve_by=preserve_by)
            mapping_groups = {
                group: {**parameters, "data": data.filter(parameters.get("predicate"))}
                for group, parameters in mapping.items()
            }
            assert_groups(groups=mapping_groups)
            return mapping_groups

        def apply_mapping(
            data: DataFrame,
            groups: dict,
            preserve_order: bool = preserve_order,
            column_extract: str = column_extract,
        ) -> dict:
            """Parse fields based on mapping"""
            return {
                group: parse_fixed_width_fields(
                    data=parameters.get("data"),
                    column_mapping=parameters.get("column_mapping"),
                )
                for group, parameters in groups.items()
            }

        def union_mapping(mapped_data: dict[str, DataFrame]) -> DataFrame:
            union_func = functools.partial(
                DataFrame.unionByName, allowMissingColumns=True
            )
            return (
                functools.reduce(union_func, mapped_data.values())
                .drop("_partition_id", "_count", "_row_number_within_partition")
                .orderBy("_row_number")
            )

        mapped_data = apply_mapping(data=data, groups=bucket_groups())
        if preserve_order:
            return union_mapping(mapped_data=mapped_data)
        return mapped_data

    if isinstance(column_mapping, dict):
        return dynamic_readin(data=data, column_mapping=column_mapping)
    return parse_fixed_width_fields(data).drop(column_extract if drop_extract else "")
