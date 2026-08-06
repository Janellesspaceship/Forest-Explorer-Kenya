import json
import os
import pandas as pd


# Read the raw IUCN JSON file

with open("data/raw/iucn_raw.json", "r") as f:
    data = json.load(f)

records = []


# Extract useful fields

for item in data:

    taxon = item.get("taxon", {})

    # Red List category
    rl_category = ""
    if taxon.get("rl_category"):
        rl_category = taxon["rl_category"].get("code")

    # Population trend
    population_trend = ""
    if taxon.get("population"):
        population_trend = taxon["population"].get("trend")

    # Assessment year
    assessment_year = None
    if taxon.get("assessment_date"):
        assessment_year = str(taxon["assessment_date"])[:4]

    record = {
        "sis_id": taxon.get("sis_id"),
        "scientific_name": taxon.get("scientific_name"),
        "kingdom": taxon.get("kingdom_name"),
        "phylum": taxon.get("phylum_name"),
        "class": taxon.get("class_name"),
        "order": taxon.get("order_name"),
        "family": taxon.get("family_name"),
        "genus": taxon.get("genus_name"),
        "species": taxon.get("species_name"),
        "authority": taxon.get("authority"),
        "common_name": "",
        "red_list_category": rl_category,
        "population_trend": population_trend,
        "assessment_year": assessment_year,
    }

    # Get first English common name
    common_names = taxon.get("common_names", [])

    for name in common_names:
        if name.get("language") == "eng":
            record["common_name"] = name.get("name")
            break

    records.append(record)


# Create DataFrame

df = pd.DataFrame(records)

print("\nPreview:")
print(df.head())

print("\nShape:", df.shape)


# Create processed folder

os.makedirs("data/processed", exist_ok=True)


# Save as Parquet

output_file = "data/processed/iucn_clean.parquet"

df.to_parquet(output_file, index=False)

print(f"\nSaved cleaned data to {output_file}")