import pathlib

import pytest
# from pyspark.testing import assertDataFrameEqual

from cdm_tools.core.normalize import normalize_data


@pytest.fixture
def spark_fixture():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col

    FILEPATH_TEST_DATA = pathlib.Path("tests/source/ELITE_JEDATA.csv")

    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    sample_data = spark.read.option("header", True).csv(FILEPATH_TEST_DATA.__str__())
    yield sample_data


class TestNormalization:
    @pytest.mark.parametrize(
        "repl_char, str_case, expected_columns",
        [
            (
                "_",
                "lower",
                [
                    "entity",
                    "account_number",
                    "account_name",
                    "acct_type",
                    "batchno",
                    "comment",
                    "amount",
                    "document_date",
                    "jrnl_no",
                    "trans_type",
                    "on_hold",
                    "period",
                    "posted_date",
                    "posted",
                    "project_nu",
                    "rev",
                    "tax_only",
                    "trandesc",
                    "effective_date",
                    "userid",
                    "approver_id",
                ],
            ),
            (
                "-",
                "lower",
                [
                    "entity",
                    "account-number",
                    "account-name",
                    "acct-type",
                    "batchno",
                    "comment",
                    "amount",
                    "document-date",
                    "jrnl-no",
                    "trans-type",
                    "on-hold",
                    "period",
                    "posted-date",
                    "posted",
                    "project-nu",
                    "rev",
                    "tax-only",
                    "trandesc",
                    "effective-date",
                    "userid",
                    "approver-id",
                ],
            ),
            (
                "_",
                "upper",
                [
                    "ENTITY",
                    "ACCOUNT_NUMBER",
                    "ACCOUNT_NAME",
                    "ACCT_TYPE",
                    "BATCHNO",
                    "COMMENT",
                    "AMOUNT",
                    "DOCUMENT_DATE",
                    "JRNL_NO",
                    "TRANS_TYPE",
                    "ON_HOLD",
                    "PERIOD",
                    "POSTED_DATE",
                    "POSTED",
                    "PROJECT_NU",
                    "REV",
                    "TAX_ONLY",
                    "TRANDESC",
                    "EFFECTIVE_DATE",
                    "USERID",
                    "APPROVER_ID",
                ],
            ),
        ],
    )
    def test_normalized_columns(
        self, spark_fixture, repl_char, str_case, expected_columns
    ):
        normalized_dataframe = normalize_data(spark_fixture, repl_char, str_case)
        assert set(normalized_dataframe.columns).difference(expected_columns) == set()

    def test_trimmed_values(self, spark_fixture):
        assert True
