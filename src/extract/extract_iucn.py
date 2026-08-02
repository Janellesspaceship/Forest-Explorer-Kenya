# Imports

import os
import json
import requests

from dotenv import load_dotenv
from google.cloud import bigquery


# Load environment variables

load_dotenv()

API_TOKEN = os.getenv("IUCN_API_TOKEN")

BASE_URL = "https://api.iucnredlist.org/api/v4"

headers = {
    "Authorization": API_TOKEN
}


# Create BigQuery client

client = bigquery.Client(project="africas-talking-bwai")


# Read species from BigQuery

query = """
SELECT species_name
FROM `africas-talking-bwai.forest_explorer.species_clean`
LIMIT 10
"""

species_df = client.query(query).to_dataframe()

print("Species retrieved from BigQuery:")
print(species_df)


# Extract data from IUCN API

results = []

for scientific_name in species_df["species_name"]:

    # Skip invalid names
    if len(scientific_name.split()) != 2:
        print(f"Skipping invalid name: {scientific_name}")
        continue

    genus_name, species_name = scientific_name.split()

    print(f"\nSearching: {scientific_name}")

    response = requests.get(
        f"{BASE_URL}/taxa/scientific_name",
        headers=headers,
        params={
            "genus_name": genus_name,
            "species_name": species_name
        }
    )

    print("Status:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        results.append(data)

        print("✓ Success")

    else:

        print("✗ Failed")
        print(response.text)


# Save results as JSON

os.makedirs("data/raw", exist_ok=True)

output_file = "data/raw/iucn_raw.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print("\n")
print(f"Downloaded {len(results)} assessments.")
print(f"Saved to {output_file}")
print("====")