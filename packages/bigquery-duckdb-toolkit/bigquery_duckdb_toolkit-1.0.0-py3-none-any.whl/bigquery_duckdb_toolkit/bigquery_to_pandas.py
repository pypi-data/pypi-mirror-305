import google.auth
import pandas as pd
from google.cloud import bigquery


class BigQueryToPandas:
    def __init__(self, project_id):
        credentials, project = google.auth.default()
        self.client = bigquery.Client(credentials=credentials, project=project_id)

    def get_partition_column(self, table_name):
        """
        Infers the partition column of a BigQuery table using INFORMATION_SCHEMA.

        Args:
            table_name (str): Name of the table in the format `project.dataset.table`.

        Returns:
            str: Name of the partition column, or None if not found.
        """
        query = f"""
        SELECT column_name
        FROM `{table_name.split('.')[0]}.{table_name.split('.')[1]}.INFORMATION_SCHEMA.COLUMNS`
        WHERE is_partitioning_column = 'YES'
        """
        result = self.client.query(query).result()
        partition_column = next((row['column_name'] for row in result), None)
        return partition_column

    def load_bigquery_table(self, table_name, filters=None):
        """
        Loads data from a BigQuery table into a pandas DataFrame with optional filtering.

        Args:
            table_name (str): Name of the table in the format `project.dataset.table`.
            filters (dict): Dictionary of filters to apply in the format {"column": "value"}.

        Returns:
            pd.DataFrame: DataFrame containing the filtered table data.
        """
        filter_conditions = " AND ".join([f"{col} = '{val}'" for col, val in (filters or {}).items()])
        query = f"SELECT * FROM `{table_name}`" + (f" WHERE {filter_conditions}" if filter_conditions else "")
        df = self.client.query(query).to_dataframe()
        return df

    def convert_data_types(self, df):
        """
        Converts specific data types in the DataFrame, adjusting datetime for timezone and dbdate to string.

        Args:
            df (pd.DataFrame): DataFrame to have data types adjusted.

        Returns:
            pd.DataFrame: DataFrame with converted data types.
        """
        for column in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[column]):
                if df[column].dtype.tz is not None:
                    df[column] = df[column].dt.tz_localize(None)
                df[column] = df[column].astype('datetime64[ns]')
            elif df[column].dtype.name == 'dbdate':
                df[column] = df[column].astype(str)
        return df
