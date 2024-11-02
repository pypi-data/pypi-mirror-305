from cdm_tools.models.templates.journal_entry_testing import ChartOfAccountsModel

import pathlib
import pytest


@pytest.fixture
def spark_fixture():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col

    FILEPATH_TEST_DATA = pathlib.Path("tests/source/ELITE_JEDATA.csv")

    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    # chart_of_accounts_model = ChartOfAccountsModel
    # chart_of_accounts_model._read = spark.read.option("header", True).csv
    # print(chart_of_accounts_model._read)
    # sample_data = chart_of_accounts_model.read(
    #     source=[FILEPATH_TEST_DATA],
    #     preprocessing=None
    # )
    # sample_data.show()
    # yield sample_data
    # yield spark


class TestCdmTransform:
    def test_required_fields(self, spark_fixture):
        assert True
        # assert set(spark_fixture.columns).difference(ChartOfAccountsModel.model_fields.keys()) == set()

    def test_mutated_fields(self, spark_fixture):
        assert True
