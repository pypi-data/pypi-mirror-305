from typing import Optional
from pyspark.sql import Row, Column, DataFrame, Window, functions as F


def retain_values(
    data: DataFrame,
    columns: list[str],
    order_by: Optional[str | list[str]] = "_row_number",
) -> DataFrame:
    """For a given column(s), forward fill all values to replace null values.

    Parameters
    ==========
    data: DataFrame
        PySpark DataFrame
    columns: list[str]
        List of column(s) to retain values. All columns must exist in data.
    order_by: Optional[str | list[str]]
        Column(s) to order the partitions by. By default, the "_row_number" column
        is used to preserve the order of the original data. This is a design feature
        specific to `cp_read_fwf` for now.

    Returns
    =======
    DataFrame
        PySpark DataFrame with column(s) forward-filled.

    Notes
    =====
    Contributed by Andy Peterson.
    Repurposed for cp_read_fwf by Lucas Nelson.
    """
    window_spec = Window.orderBy(order_by)
    assert all(
        column in data.columns for column in columns
    ), "At least one column does not appear in the data."
    return data.withColumns(
        {
            column: F.last(column, ignorenulls=True).over(window_spec)
            for column in columns
        }
    )


def assign_row_number(
    data: DataFrame,
    preserve_by: Optional[Column] = F.lit(1),
    n_partitions: Optional[int] = None,
) -> DataFrame:
    """
    Deterministically assign a row number in a distributed environment.

    Given a DataFrame, this function ensures a sequential ID is generated regardless
    of the number of partitions (if any). This is done in the following manner:
        + partition the DataFrame
        + aggregate to obtain endpoints of each partition
        + assign row ID per partition, scaled by partition's endpoint

    As a sanity check, users can confirm the row ID is assigned sequentially by running
    the following summary:
    >>> (
        assign_row_number(data=data)
        .groupby(spark_partition_id())
        .agg(min("_row_number"), max("_row_number"))
    )

    Parameters
    ==========
    data: DataFrame
        PySpark DataFrame to assign row number.
    preserve_by: Optional[Column]
        Name of column to preserve the row number by. Default is to preserve by all columns. If
        appropriate, specify the column to order by as `F.col("<column_name>")`.
    n_partitions: Optional[int]
        Number of partitions to distribute data across. By default, this number is determined
        by Spark. If appropriate, specify your number of partitions as a positive integer here.

    Returns
    =======
    DataFrame
        PySpark DataFrame containing the "_row_number" column.

    Examples
    ========
    # attach row number to DataFrame
    >>> assign_row_number(data=data)

    # attach row number to DataFrame based on order of a column(s)
    >>> assign_row_number(data=data, preserve_by=F.col("<column_name>"))
    >>> assign_row_number(data=data, preserve_by=[F.col("<column_name>"), F.col("<column_name>"), ...])

    # attach row number to DataFrame on single or multiple node(s)
    >>> assign_row_number(data=data, n_partitions=1)
    >>> assign_row_number(data=data, n_partitions=110799)

    Notes
    =====
    This method is sourced from the following link:
    https://medium.com/@aalopatin/row-number-in-spark-is-simple-but-there-are-nuances-a7c9099e55dc
    """

    # partition the data according to Spark's default partitioning mechanism;
    # allow user to (optionally) specify number of partitions
    if n_partitions:
        data = data.repartition(n_partitions)
    data_cached = data.withColumn("_partition_id", F.spark_partition_id()).cache()

    # summarize how many rows appear in each partition; generated "_count"
    # column shows count per partition (should be roughly uniform) which
    # acts as a proxy for the maximum row number assigned per partition
    data_partitioned = (
        data_cached.select("_partition_id")
        .groupby("_partition_id")
        .agg(F.count("*").alias("_count"))
        .withColumn(
            "_count",
            F.sum(F.col("_count")).over(Window.orderBy("_partition_id"))
            - F.col("_count"),
        )
    )

    # assign a row count per partition and scale by number of total rows
    # in partition to ensure no overlap across partitions; data is sorted
    # by row number as a final step
    return (
        data_cached.join(F.broadcast(data_partitioned), ["_partition_id"])
        .withColumn(
            "_row_number_within_partition",
            F.row_number().over(
                Window.partitionBy("_partition_id").orderBy(preserve_by)
            ),
        )
        .withColumn(
            "_row_number", F.col("_count") + F.col("_row_number_within_partition")
        )
        .orderBy("_row_number")
        .drop("_count", "_partition_id", "_row_number_within_partition")
        .cache()
    )


def test_assign_row_number(
    data: Optional[DataFrame] = None,
    schema: Optional[dict] = None,
    n_rows: Optional[int] = 10_000,
    n_partitions: Optional[int] = None,
) -> None:
    """
    Ensure row numbers generate in sequential manner. Multiple test cases are performed:
        1. Validate underlying data is not altered by `assign_row_number()` function
        2. Validate `assign_row_number()` function generates unique identifier.
        3. Validate `assign_row_number()` function generates sequential identifier.
        4. Validate transformations before/after `assign_row_number()` function do not
           alter the previous tests (aka. caching preserves state).

    If all tests pass, it can be determined that the `assign_row_number()` function is a
    reliable function for generating a row ID for any DataFrame until proven otherwise.

    Parameters
    ==========
    data: Optional[DataFrame]
        Data to generate sequential row number. If not passed, schema will be used.
    schema: Optional[dict]
        Dictionary containing column-range pairings. If not passed, the sample schema
        will be used.
    n_rows: Optional[int]
        Number of rows to generate in sample data.
    n_partitions: Optional[int]
        Number of partitions to distribute data across.

    Returns
    =======
    None
        This function simply asserts whether or not this function can generate row
        numbers in a deterministic, sequential manner. It is meant to be called to
        ensure the function works "as expected".
    """

    import random
    import string

    from pyspark.testing import assertDataFrameEqual

    import pyspark.pandas as ps

    SAMPLE_SCHEMA: dict = {
        "account_number": range(5),
        "fiscal_year": range(1999, 2024),
        "fiscal_period": range(1, 13),
        "journal_number": [
            "".join(random.choices(string.ascii_uppercase, k=10)) for _ in range(5)
        ],
    }

    def generate_sample_data(schema: dict, n_rows: int) -> DataFrame:
        """Generate DataFrame using provided schema"""
        schema = {
            column: [random.choice(values) for _ in range(n_rows)]
            for column, values in schema.items()
        }
        return ps.DataFrame(schema).to_spark()

    def assert_expectations(
        data: DataFrame, data_indexed: DataFrame, column_index: str = "_row_number"
    ) -> None:
        DATA_COUNT: int = data.count()

        def assert_identical_data() -> None:
            """Validate indexed data is identical to input data."""
            try:
                assertDataFrameEqual(data, data_indexed.drop(column_index))
                print("[SUCCESS] Function does not modify underlying data.")
            except AssertionError:
                print("[FAIL] Function modifies underlying data.")
            except Exception as e:
                raise e

        def assert_unique_identifier() -> None:
            """Validate indexed data assigns a unique identifier per observation."""
            try:
                assert (
                    data_indexed.select(column_index).distinct().count() == DATA_COUNT
                )
                print(
                    f"[SUCCESS] Function generates unique identifier. [1, {DATA_COUNT:,}]"
                )
            except AssertionError:
                print("[FAIL] Function does not generate unique identifier.")
            except Exception as e:
                raise e

        def assert_sequential_ordering() -> None:
            def _collect_value_from_row(row: Row, column_name: str):
                """Return value in row as scalar value."""
                assert len(row) == 1
                return row[0][column_name]

            def summarize_by_partition(data: DataFrame) -> DataFrame:
                """Gather summary of index by partition."""
                return (
                    assign_row_number(data=data)
                    .groupby(F.spark_partition_id())
                    .agg(
                        F.count("*").alias("partition_count"),
                        F.min("_row_number").alias("partition_min"),
                        F.max("_row_number").alias("partition_max"),
                    )
                )

            def assert_shape_preserved(partition_summary: DataFrame) -> None:
                """Validate number of rows across partitions matches total number of rows."""
                try:
                    partition_total_rows = _collect_value_from_row(
                        partition_summary.agg(
                            F.sum("partition_count").alias("partition_count")
                        ).collect(),
                        "partition_count",
                    )
                    assert partition_total_rows == DATA_COUNT
                except AssertionError:
                    print("[ERROR] The number of rows changed while testing.")
                except Exception as e:
                    raise e

            def assert_min_max_sequential(partition_summary: DataFrame) -> None:
                """Validate the partition N starts where partition M ends, where M < N."""
                try:
                    assertDataFrameEqual(
                        (
                            partition_summary.select(
                                F.explode(
                                    F.array("partition_min", "partition_max")
                                ).alias("row_sequence")
                            )
                        ),
                        (
                            partition_summary.select(
                                F.explode(
                                    F.array("partition_min", "partition_max")
                                ).alias("row_sequence")
                            ).orderBy("row_sequence")
                        ),
                    )
                    print(
                        "[SUCCESS] Function generates row number in a sequential order."
                    )
                except AssertionError:
                    print(
                        "[FAIL] Function does not generate row number in a sequential order."
                    )
                except Exception as e:
                    raise e

            partition_summary = summarize_by_partition(data)
            assert_shape_preserved(partition_summary)
            assert_min_max_sequential(partition_summary)

        def assert_preserved_state(
            transformation: Column = lambda data: data.select("*"),
        ) -> None:
            """Validate caching the resulting indexed data preserves a sequential ordering."""
            try:
                # case 1: data transformed before ordering
                data_transformed = transformation(data)
                assertDataFrameEqual(
                    transformation(data_transformed),
                    transformation(data_indexed).drop(column_index),
                )

                # case 2: data transformed after ordering
                data_transformed = transformation(data_indexed)
                assertDataFrameEqual(data_transformed, data_indexed)
                print("[SUCCESS] Function caches data successfully.")
            except AssertionError:
                print("[FAIL] Function does not cache data successfully.")
            except Exception as e:
                raise e

        # run all test cases against data
        assert_identical_data()
        assert_unique_identifier()
        assert_sequential_ordering()
        assert_preserved_state()

    if data is None:
        schema = SAMPLE_SCHEMA if schema is None else schema
        data = generate_sample_data(schema=schema, n_rows=n_rows)

    if n_partitions:
        data = data.repartition(n_partitions)

    assert_expectations(
        data=data, data_indexed=assign_row_number(data=data.drop("_row_number"))
    )
