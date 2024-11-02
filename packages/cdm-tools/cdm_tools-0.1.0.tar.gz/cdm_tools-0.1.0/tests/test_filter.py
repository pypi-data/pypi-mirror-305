import pathlib

import pytest

from cdm_tools.core.normalize import normalize_data
from cdm_tools.core.filter import (
    filter_nulls,
    filter_range,
    filter_regex,
    filter_substring,
)


@pytest.fixture
def spark_fixture():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col

    FILEPATH_TEST_DATA = pathlib.Path("tests/source/ELITE_JEDATA.csv")

    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    sample_data = spark.read.option("header", True).csv(FILEPATH_TEST_DATA.__str__())
    yield normalize_data(sample_data)


class TestFilter:
    def test_filter_predicate(self):
        assert True

    @pytest.mark.parametrize(
        "columns, expected_row_count, predicate_kwargs",
        [
            # filtering non-null columns for null pairs
            (["entity", "account_number"], 15_375, dict()),
            (["entity", "account_number", "approver_id"], 15_375, dict()),
            (["entity", "account_number", "approver_id"], 15_375, {"strict": True}),
            (["entity", "account_number", "approver_id"], 6_887, {"strict": False}),
            (
                ["entity", "account_number", "approver_id"],
                15_375 - 6_887,
                {"strict": False, "negate": True},
            ),
            (["entity", "account_number"], 0, {"strict": True, "negate": True}),
        ],
    )
    def test_filter_nulls(
        self, spark_fixture, columns, expected_row_count, predicate_kwargs
    ):
        sampled_data = filter_nulls(spark_fixture, columns, **predicate_kwargs)
        assert sampled_data.count() == expected_row_count

    @pytest.mark.parametrize(
        "columns, pattern, expected_row_count, predicate_kwargs",
        [
            # filtering non-null columns for null pairs
            (["entity", "account_number"], r"^[a-zA-Z\d]+$", 0, dict()),
            # (
            #     ["entity", "account_number", "approver_id"],
            #     r"^[a-zA-Z\d]+$",
            #     15_375 - 6_887,
            #     {"negate": True},
            # ),
            (
                ["entity", "account_number", "approver_id"],
                r"^[a-zA-Z\d]+$",
                15_375,
                {"negate": True},
            ),
            (
                ["entity", "account_number", "approver_id"],
                r"^[a-zA-Z\d]+$",
                15_375,
                {"strict": False},
            ),
        ],
    )
    def test_filter_regex(
        self, spark_fixture, columns, pattern, expected_row_count, predicate_kwargs
    ):
        sampled_data = filter_regex(spark_fixture, columns, pattern, **predicate_kwargs)
        assert sampled_data.count() == expected_row_count
