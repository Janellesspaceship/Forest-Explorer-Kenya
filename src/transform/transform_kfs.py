"""
transform_kfs.py

Transforms Kenya Forest Service (KFS) spatial datasets into clean,
analysis-ready Parquet files for BigQuery and Streamlit.

Datasets processed:
1. Gazetted Forests
2. Protected Areas
3. Forest Types (2010)
4. KFS Forest Boundaries
"""

# Import Libraries

import os
import geopandas as gpd


# Create output directory if it doesn't exist


os.makedirs("data/processed/kfs", exist_ok=True)


# Helper Function


def clean_dataset(
    input_file,
    output_file,
    columns_to_keep,
    rename_dict,
    calculate_area=False,
    source=None
):
    """
    Reads a GeoJSON dataset, cleans it,
    optionally calculates area,
    optionally adds a data source,
    and saves it as a Parquet file.
    """

    print("\n" + "=" * 70)
    print(f"Reading: {input_file}")

    
    # Read GeoJSON
    
    gdf = gpd.read_file(input_file)

    print(f"Loaded {len(gdf)} records.")

    
    # Keep only required columns
    
    gdf = gdf[columns_to_keep]

    # Rename columns
    
    gdf = gdf.rename(columns=rename_dict)

    
    # Convert CRS to WGS84 if necessary
    

    if gdf.crs is not None:
        gdf = gdf.to_crs(epsg=4326)


    # Remove duplicate records
    

    gdf = gdf.drop_duplicates()

    
    # Calculate area in square kilometres (optional)
    

    if calculate_area:

        projected = gdf.to_crs(epsg=21037)

        gdf["area_sq_km"] = projected.area / 1_000_000

   
    # Add data source (optional)
    
    if source is not None:
        gdf["source"] = source

    
    # Preview cleaned dataset
   
    print("\nPreview:")
    print(gdf.head())

    print("\nShape:", gdf.shape)

    print("\nColumns:")
    print(gdf.columns.tolist())


    # Save as Parquet
    

    gdf.to_parquet(output_file, index=False)

    print(f"\nSaved to {output_file}")


# 1. Gazetted Forests

clean_dataset(

    input_file="data/raw/kfs/kenya_gazetted_forest_-2241218727256807108.geojson",

    output_file="data/processed/kfs/kfs_gazetted.parquet",

    columns_to_keep=[
        "FOREST",
        "GAZETTED",
        "area",
        "geometry"
    ],

    rename_dict={
        "FOREST": "forest_name",
        "GAZETTED": "gazetted",
        "area": "area"
    },

    source="Kenya Forest Service"

)


# 2. Protected Areas

clean_dataset(

    input_file="data/raw/kfs/protected_area.geojson",

    output_file="data/processed/kfs/kfs_protected.parquet",

    columns_to_keep=[
        "AREANAME",
        "SIZE",
        "YEAR",
        "IUCNCAT",
        "CNTRYNAME",
        "geometry"
    ],

    rename_dict={
        "AREANAME": "protected_area",
        "SIZE": "size",
        "YEAR": "year_established",
        "IUCNCAT": "iucn_category",
        "CNTRYNAME": "country"
    },

    source="Kenya Forest Service"

)


# 3. Forest Types (2010)

clean_dataset(

    input_file="data/raw/kfs/Kenya_Forest_Type_2010_Dataset.geojson",

    output_file="data/processed/kfs/kfs_forest_types.parquet",

    columns_to_keep=[
        "OBJECTID",
        "FORE_TY_10",
        "Area",
        "geometry"
    ],

    rename_dict={
        "OBJECTID": "object_id",
        "FORE_TY_10": "forest_type",
        "Area": "area"
    },

    source="Kenya Forest Service"

)


# 4. KFS Forest Boundaries

clean_dataset(

    input_file="data/raw/kfs/kfs_raw.geojson",

    output_file="data/processed/kfs/kfs_boundaries.parquet",

    columns_to_keep=[
        "AREA",
        "geometry"
    ],

    rename_dict={
        "AREA": "area_original"
    },

    calculate_area=True,

    source="Kenya Forest Service"

)


# Finished


print("\n" + "=" * 70)
print("KFS transformation completed successfully!")
print("=" * 70)