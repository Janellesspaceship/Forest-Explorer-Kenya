import requests
import json
from pathlib import Path

URL = "https://api.gbif.org/v1/occurrence/search"

params = {
    "country": "KE",
    "limit": 10
}

response = requests.get(URL, params=params, timeout=30)
response.raise_for_status()

data = response.json()

print(f"Status code: {response.status_code}")
print(f"Records returned: {len(data['results'])}")

# Create output folder
output_dir = Path("data/raw/gbif")
output_dir.mkdir(parents=True, exist_ok=True)

# Save the untouched API response
with open(output_dir / "gbif_test.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Raw GBIF data saved successfully!")