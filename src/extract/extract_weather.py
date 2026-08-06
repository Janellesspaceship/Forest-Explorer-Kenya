"""
extract_weather.py

Extracts current weather data for major Kenyan forests
from the OpenWeather API and saves the raw JSON responses.
"""


# Imports


import json
from pathlib import Path

import requests
from dotenv import dotenv_values


# Project Directories


BASE_DIR = Path(__file__).resolve().parents[2]

ENV_FILE = BASE_DIR / ".env"

RAW_DIR = BASE_DIR / "data" / "raw" / "weather"
RAW_DIR.mkdir(parents=True, exist_ok=True)


# Load Environment Variables

env_values = dotenv_values(ENV_FILE)

API_KEY = env_values.get("OPENWEATHER_API_KEY")

print("=" * 70)
print("Project Directory :", BASE_DIR)
print(".env Location     :", ENV_FILE)
print(".env Exists       :", ENV_FILE.exists())
print("Environment Values:", env_values)
print("API Loaded        :", API_KEY is not None)
print("=" * 70)

if not API_KEY:
    raise ValueError(
        f"OPENWEATHER_API_KEY not found.\n"
        f"Expected in:\n{ENV_FILE}"
    )


# OpenWeather API


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Kenyan Forest Coordinates


FORESTS = [
    {"forest": "Kakamega Forest", "lat": 0.2827, "lon": 34.8664},
    {"forest": "Mau Forest", "lat": -0.4500, "lon": 35.6500},
    {"forest": "Aberdare Forest", "lat": -0.3900, "lon": 36.6500},
    {"forest": "Mount Kenya Forest", "lat": -0.1520, "lon": 37.3080},
    {"forest": "Arabuko Sokoke Forest", "lat": -3.3000, "lon": 39.9800},
    {"forest": "Karura Forest", "lat": -1.2450, "lon": 36.8210},
    {"forest": "Ngong Road Forest", "lat": -1.3180, "lon": 36.7630},
    {"forest": "Shimba Hills Forest", "lat": -4.2500, "lon": 39.3830},
]


# Extract Weather Data


print("\n" + "=" * 70)
print("Extracting weather data...")
print("=" * 70)

for forest in FORESTS:

    print(f"\nGetting weather for {forest['forest']}...")

    try:

        response = requests.get(
            BASE_URL,
            params={
                "lat": forest["lat"],
                "lon": forest["lon"],
                "appid": API_KEY,
                "units": "metric",
            },
            timeout=30,
        )

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("Request failed:")
            print(response.text)
            continue

        weather = response.json()
        weather["forest_name"] = forest["forest"]

        filename = (
            forest["forest"]
            .lower()
            .replace(" ", "_")
            .replace("-", "_")
            + ".json"
        )

        output_file = RAW_DIR / filename

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(weather, f, indent=4)

        print(f"Saved -> {output_file.name}")

    except Exception as e:
        print(f"Error retrieving {forest['forest']}: {e}")

print("\n" + "=" * 70)
print("Weather extraction completed successfully!")
print("=" * 70)