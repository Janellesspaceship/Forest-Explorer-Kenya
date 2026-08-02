from google.cloud import bigquery

# Create BigQuery client
client = bigquery.Client(project="africas-talking-bwai")

# Path to the Parquet file
file_path = "data/processed/gbif_clean.parquet"

# Destination table
table_id = "africas-talking-bwai.forest_explorer.species"

# Configure the load job
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition="WRITE_TRUNCATE",
)

# Upload the file
with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config,
    )

job.result()

print(f"Successfully loaded data into {table_id}")