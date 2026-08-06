from google.cloud import bigquery
import pandas as pd


# Create BigQuery client

client = bigquery.Client(project="africas-talking-bwai")


# Read cleaned parquet

df = pd.read_parquet("data/processed/iucn_clean.parquet")

print(df.head())
print(df.shape)


# Destination table

table_id = "africas-talking-bwai.forest_explorer.iucn"


# Configure the load job

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE"
)


# Upload dataframe

job = client.load_table_from_dataframe(
    df,
    table_id,
    job_config=job_config
)

job.result()

print(f"Loaded {job.output_rows} rows into {table_id}")