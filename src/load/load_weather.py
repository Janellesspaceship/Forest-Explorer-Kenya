"""
load_weather.py

Uploads the processed weather dataset
to Google BigQuery.

"""


# Imports


from pathlib import Path

import pandas as pd
from google.cloud import bigquery



# Project Directories


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data" / "processed" / "weather"

print("=" * 70)
print("Project Directory :", BASE_DIR)
print("Data Directory    :", DATA_DIR)
print("Exists            :", DATA_DIR.exists())

if DATA_DIR.exists():
    print("\nFiles Found:")
    for file in DATA_DIR.iterdir():
        print("-", file.name)

print("=" * 70)



# BigQuery Configuration


PROJECT_ID = "africas-talking-bwai"
DATASET_ID = "forest_explorer"

client = bigquery.Client(project=PROJECT_ID)



# Upload Function


def upload_parquet(parquet_file, table_name):
    """
    Upload a Parquet file to BigQuery.
    """

    print("\n" + "=" * 70)
    print(f"Uploading {parquet_file.name}")

    if not parquet_file.exists():
        print(f"ERROR: {parquet_file} not found.")
        return

    df = pd.read_parquet(parquet_file)

    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result()

    print("Upload Complete!")
    print(f"Table: {table_id}")



# Upload Weather Dataset


upload_parquet(
    DATA_DIR / "weather.parquet",
    "weather"
)



# Finished


print("\n" + "=" * 70)
print("Weather dataset uploaded successfully!")
print("=" * 70)