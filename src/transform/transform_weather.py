"""
transform_weather.py

Reads raw OpenWeather JSON files, cleans the data,
and saves a single Parquet dataset.

"""


# Imports

import json
from pathlib import Path

import pandas as pd



# Project Directories


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DIR = BASE_DIR / "data" / "raw" / "weather"

PROCESSED_DIR = BASE_DIR / "data" / "processed" / "weather"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)



# Read JSON Files

weather_records = []

print("=" * 70)
print("Transforming Weather Data")
print("=" * 70)

json_files = list(RAW_DIR.glob("*.json"))

print(f"Found {len(json_files)} JSON files.\n")



# Process Each File


for file in json_files:

    print(f"Reading {file.name}")

    with open(file, "r", encoding="utf-8") as f:
        weather = json.load(f)

    record = {
        "forest_name": weather.get("forest_name"),

        "city": weather.get("name"),

        "country": weather.get("sys", {}).get("country"),

        "latitude": weather.get("coord", {}).get("lat"),

        "longitude": weather.get("coord", {}).get("lon"),

        "temperature": weather.get("main", {}).get("temp"),

        "feels_like": weather.get("main", {}).get("feels_like"),

        "temp_min": weather.get("main", {}).get("temp_min"),

        "temp_max": weather.get("main", {}).get("temp_max"),

        "pressure": weather.get("main", {}).get("pressure"),

        "humidity": weather.get("main", {}).get("humidity"),

        "weather": weather.get("weather", [{}])[0].get("main"),

        "description": weather.get("weather", [{}])[0].get("description"),

        "wind_speed": weather.get("wind", {}).get("speed"),

        "wind_direction": weather.get("wind", {}).get("deg"),

        "cloudiness": weather.get("clouds", {}).get("all"),

        "visibility": weather.get("visibility"),

        "sunrise": weather.get("sys", {}).get("sunrise"),

        "sunset": weather.get("sys", {}).get("sunset"),

        "timestamp": weather.get("dt"),
    }

    weather_records.append(record)



# Create DataFrame

weather_df = pd.DataFrame(weather_records)

print("\nData Preview")
print(weather_df.head())



# Convert Unix Time


weather_df["timestamp"] = pd.to_datetime(
    weather_df["timestamp"],
    unit="s"
)

weather_df["sunrise"] = pd.to_datetime(
    weather_df["sunrise"],
    unit="s"
)

weather_df["sunset"] = pd.to_datetime(
    weather_df["sunset"],
    unit="s"
)



# Save Parquet


output_file = PROCESSED_DIR / "weather.parquet"

weather_df.to_parquet(
    output_file,
    index=False
)

print("\n" + "=" * 70)
print("Transformation Complete!")
print(f"Rows      : {len(weather_df)}")
print(f"Columns   : {len(weather_df.columns)}")
print(f"Saved to  : {output_file}")
print("=" * 70)