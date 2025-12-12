"""
Utility functions for processing bronze-layer geometries.
"""

import os
import geopandas as gpd
from pathlib import Path


def clean_name(name):
    """
    Clean filename by removing numbers and special characters.

    Parameters:
    -----------
    name : str
        Original filename

    Returns:
    --------
    str
        Cleaned name (lowercase, underscores, no numbers)
    """
    # Remove numbers and special characters, keep only letters, spaces, and underscores
    cleaned = ''.join(char for char in name if char.isalpha() or char in [' ', '_'])
    # Convert to lowercase, strip whitespace, replace spaces with underscores
    cleaned = cleaned.lower().strip().replace(' ', '_')
    # Remove any trailing underscores
    cleaned = cleaned.rstrip('_')
    return cleaned


def read_and_process_geojson(input_geojson_path, output_geoparquet_path):
    """
    Process a single GeoJSON file to GeoParquet format.

    Parameters:
    -----------
    input_geojson_path : str or Path
        Path to input GeoJSON file
    output_geoparquet_path : str or Path
        Path to output GeoParquet file
    """
    # Read the GeoJSON file
    gdf = gpd.read_file(input_geojson_path)

    # Ensure all geometries are in WGS84 (EPSG:4326)
    if gdf.crs != "EPSG:4326":
        gdf = gdf.to_crs(epsg=4326)

    # Save as GeoParquet
    gdf.to_parquet(output_geoparquet_path, compression='snappy', index=False)
    print(f"✓ Processed: {Path(input_geojson_path).name} -> {Path(output_geoparquet_path).name}")



# We should instead assume that the input and output directories are known and then the file names are passed in, no?

def process_geometry(filename, input_layer, output_layer):
    """
    Process a geometry file from one layer to another.

    Parameters:
    -----------
    filename : str
        Name of the geometry file (e.g., "Address_Points_123.geojson")
    input_layer : str
        Source layer name (e.g., "bronze")
    output_layer : str
        Destination layer name (e.g., "silver")
    """
    # Build full paths
    script_dir = Path(__file__).parent.parent.parent.parent  # Up to attempt-2/
    input_path = script_dir / "data" / input_layer / "geometries" / filename

    # Create output directory
    output_dir = script_dir / "data" / output_layer / "geometries"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create cleaned output filename
    base_name = filename.replace(".geojson", "")
    cleaned_name = clean_name(base_name)
    output_path = output_dir / f"{cleaned_name}.geoparquet"

    # Read GeoJSON
    print(f"  Reading: {filename}")
    gdf = gpd.read_file(input_path)
    print(f"    → Loaded {len(gdf)} features")

    # Convert CRS if needed
    if gdf.crs != "EPSG:4326":
        gdf = gdf.to_crs(epsg=4326)
        print("    → Converted to EPSG:4326")

    # Save as parquet
    gdf.to_parquet(output_path, compression='snappy', index=False)
    print(f"    → Saved: {cleaned_name}.geoparquet")



# def process_all_geometries(input_directory, output_directory):
#     """
#     Process all GeoJSON files in a directory to GeoParquet format.

#     Parameters:
#     -----------
#     input_directory : str or Path
#         Directory containing GeoJSON files
#     output_directory : str or Path
#         Directory to save GeoParquet files
#     """
#     input_dir = Path(input_directory)
#     output_dir = Path(output_directory)

#     # Create output directory if it doesn't exist
#     output_dir.mkdir(parents=True, exist_ok=True)

#     # Process each GeoJSON file
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".geojson"):
#             # Clean the filename
#             base_name = filename.replace(".geojson", "")
#             cleaned_name = clean_name(base_name)

#             # Set up paths
#             input_path = input_dir / filename
#             output_path = output_dir / f"{cleaned_name}.geoparquet"

#             # Process the file
#             process_geometries(input_path, output_path)
