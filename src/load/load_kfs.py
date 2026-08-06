"""
load_kfs.py

Loads cleaned Kenya Forest Service (KFS) datasets
from Parquet files into Google BigQuery.
"""

from pathlib import Path

import pandas as pd
from google.cloud import bigquery


# Find the project root automatically


current = Path(__file__).resolve()

BASE_DIR = current

while not (BASE_DIR / "data").exists():
    if BASE_DIR.parent == BASE_DIR:
        raise FileNotFoundError("Could not find the project root containing the 'data' folder.")
    BASE_DIR = BASE_DIR.parent

print("=" * 70)
print("Project Root:", BASE_DIR)


# Processed KFS data directory

DATA_DIR = BASE_DIR / "data" / "processed" / "kfs"

print("KFS Data Directory:", DATA_DIR)
print("Directory exists:", DATA_DIR.exists())

if not DATA_DIR.exists():
    raise FileNotFoundError(f"KFS directory not found:\n{DATA_DIR}")

print("\nFiles found:")

for file in DATA_DIR.glob("*.parquet"):
    print(f"  • {file.name}")

print("=" * 70)


# BigQuery Configuration


PROJECT_ID = "africas-talking-bwai"
DATASET_ID = "forest_explorer"

client = bigquery.Client(project=PROJECT_ID)


# Upload Function

def upload_parquet(filename, table_name):
    """
    Upload a Parquet file to BigQuery.
    """

    parquet_file = DATA_DIR / filename

    print("\n" + "=" * 70)
    print(f"Uploading: {filename}")

    print("Full path:")
    print(parquet_file)

    if not parquet_file.exists():
        raise FileNotFoundError(
            f"\nFile not found:\n{parquet_file}"
        )

    df = pd.read_parquet(parquet_file)

    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config,
    )

    job.result()

    print(f"✓ Uploaded {len(df):,} rows")
    print(f"✓ Table: {table_id}")


# Upload all KFS datasets


upload_parquet("kfs_gazetted.parquet", "kfs_gazetted")

upload_parquet("kfs_protected.parquet", "kfs_protected")

upload_parquet("kfs_forest_types.parquet", "kfs_forest_types")

upload_parquet("kfs_boundaries.parquet", "kfs_boundaries")


# Finished

print("\n" + "=" * 70)
print("✓ All KFS datasets uploaded successfully!")
print("=" * 70)