import pandas as pd
import sqlalchemy.dialects.postgresql as POSTGRESQL_TYPES

import great_expectations.expectations as gxe
from great_expectations.compatibility.snowflake import SNOWFLAKE_TYPES
from tests.integration.conftest import parameterize_batch_for_data_sources
from tests.integration.test_utils.data_source_config import (
    PandasDataFrameDatasourceTestConfig,
    PandasFilesystemCsvDatasourceTestConfig,
    PostgreSQLDatasourceTestConfig,
    SnowflakeDatasourceTestConfig,
)


@parameterize_batch_for_data_sources(
    data_source_configs=[
        PandasDataFrameDatasourceTestConfig(),
        PandasFilesystemCsvDatasourceTestConfig(),
        PostgreSQLDatasourceTestConfig(column_types={"a": POSTGRESQL_TYPES.INTEGER}),
        SnowflakeDatasourceTestConfig(column_types={"a": SNOWFLAKE_TYPES.NUMBER}),
    ],
    data=pd.DataFrame({"a": [1, 2]}),
)
def test_expect_column_min_to_be_between(batch_for_datasource) -> None:
    expectation = gxe.ExpectColumnMinToBeBetween(column="a", min_value=1, max_value=1)
    result = batch_for_datasource.validate(expectation)
    assert result.success


@parameterize_batch_for_data_sources(
    data_source_configs=[
        PandasDataFrameDatasourceTestConfig(),
        PandasFilesystemCsvDatasourceTestConfig(),
        SnowflakeDatasourceTestConfig(column_types={"a": SNOWFLAKE_TYPES.NUMBER}),
        PostgreSQLDatasourceTestConfig(column_types={"a": POSTGRESQL_TYPES.INTEGER}),
    ],
    data=pd.DataFrame({"a": [1, 2]}),
)
def test_expect_column_max_to_be_between(batch_for_datasource) -> None:
    expectation = gxe.ExpectColumnMaxToBeBetween(column="a", min_value=2, max_value=2)
    result = batch_for_datasource.validate(expectation)
    assert result.success


@parameterize_batch_for_data_sources(
    data_source_configs=[
        PandasDataFrameDatasourceTestConfig(),
        PandasFilesystemCsvDatasourceTestConfig(),
        SnowflakeDatasourceTestConfig(column_types={"a": SNOWFLAKE_TYPES.NUMBER}),
        PostgreSQLDatasourceTestConfig(column_types={"a": POSTGRESQL_TYPES.INTEGER}),
    ],
    data=pd.DataFrame({"a": [1, 2]}),
)
def test_expect_column_to_exist(batch_for_datasource):
    expectation = gxe.ExpectColumnToExist(column="a")
    result = batch_for_datasource.validate(expectation)
    assert result.success


@parameterize_batch_for_data_sources(
    data_source_configs=[
        PandasDataFrameDatasourceTestConfig(),
        PandasFilesystemCsvDatasourceTestConfig(),
        SnowflakeDatasourceTestConfig(column_types={"a": SNOWFLAKE_TYPES.NUMBER}),
        PostgreSQLDatasourceTestConfig(column_types={"a": POSTGRESQL_TYPES.INTEGER}),
    ],
    data=pd.DataFrame({"a": [1, 2]}),
)
def test_expect_column_values_to_not_be_null(batch_for_datasource):
    expectation = gxe.ExpectColumnValuesToNotBeNull(column="a")
    result = batch_for_datasource.validate(expectation)
    assert result.success


@parameterize_batch_for_data_sources(
    data_source_configs=[
        PandasDataFrameDatasourceTestConfig(),
        PandasFilesystemCsvDatasourceTestConfig(),
        SnowflakeDatasourceTestConfig(column_types={"a": SNOWFLAKE_TYPES.NUMBER}),
        PostgreSQLDatasourceTestConfig(column_types={"a": POSTGRESQL_TYPES.INTEGER}),
    ],
    data=pd.DataFrame({"a": [1, 2, 3, 4]}),
)
def test_expect_column_mean_to_be_between(batch_for_datasource):
    expectation = gxe.ExpectColumnMeanToBeBetween(column="a", min_value=2, max_value=3)
    result = batch_for_datasource.validate(expectation)
    assert result.success


class TestExpectTableRowCountToEqualOtherTable:
    @parameterize_batch_for_data_sources(
        data_source_configs=[
            PostgreSQLDatasourceTestConfig(
                column_types={"col_a": POSTGRESQL_TYPES.INTEGER},
                extra_assets={"test_table_two": {"col_b": POSTGRESQL_TYPES.VARCHAR}},
            ),
        ],
        data=pd.DataFrame({"a": [1, 2, 3, 4]}),
        extra_data={"test_table_two": pd.DataFrame({"col_b": ["a", "b", "c", "d"]})},
    )
    def test_success(self, batch_for_datasource):
        expectation = gxe.ExpectTableRowCountToEqualOtherTable(other_table_name="test_table_two")
        result = batch_for_datasource.validate(expectation)
        assert result.success

    @parameterize_batch_for_data_sources(
        data_source_configs=[
            PostgreSQLDatasourceTestConfig(
                column_types={"col_a": POSTGRESQL_TYPES.INTEGER},
                extra_assets={"test_table_two": {"col_b": POSTGRESQL_TYPES.VARCHAR}},
            ),
        ],
        data=pd.DataFrame({"a": [1, 2, 3, 4]}),
        extra_data={"test_table_two": pd.DataFrame({"col_b": ["just_this_one!"]})},
    )
    def test_different_counts(self, batch_for_datasource):
        expectation = gxe.ExpectTableRowCountToEqualOtherTable(other_table_name="test_table_two")
        result = batch_for_datasource.validate(expectation)
        assert not result.success
        assert result.result["observed_value"] == {
            "self": 4,
            "other": 1,
        }

    @parameterize_batch_for_data_sources(
        data_source_configs=[
            PostgreSQLDatasourceTestConfig(
                column_types={"col_a": POSTGRESQL_TYPES.INTEGER},
            ),
        ],
        data=pd.DataFrame({"a": [1, 2, 3, 4]}),
    )
    def test_missing_table(self, batch_for_datasource):
        expectation = gxe.ExpectTableRowCountToEqualOtherTable(other_table_name="where_am_i")
        result = batch_for_datasource.validate(expectation)
        assert not result.success, "We should not find the other table, since we didn't load it."
