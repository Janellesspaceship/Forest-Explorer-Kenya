import json

# Open the raw GBIF data
with open("data/raw/gbif/gbif_test.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Get the occurrence records
records = data["results"]

print(f"Records loaded: {len(records)}")