import re
import string
import functools

from pyspark.sql import DataFrame, functions as F


def normalize_data(
    data: DataFrame, repl_char: str = "_", str_case: str = "lower"
) -> DataFrame:
    """Trim data values and convert columns to specified case (default: lower snakecase)"""

    def normalize_columns(columns: list[str]) -> list[str]:
        """Remove invalid characters at ends, replace intermediate characters, and convert to `str_case`"""
        invalid_characters = rf"[\s{string.punctuation}]+"
        rules = (
            re.compile(f"(^{invalid_characters}|{invalid_characters}$)"),
            re.compile(invalid_characters),
        )
        return functools.reduce(
            lambda acc, rule: map(lambda column: rule.sub(repl_char, column), acc),
            rules,
            map(getattr(str, str_case), columns),
        )

    data = data.withColumns({column: F.trim(F.col(column)) for column in data.columns})
    for existing, new in zip(data.columns, normalize_columns(data.columns)):
        data = data.withColumnRenamed(existing, new)
    return data
