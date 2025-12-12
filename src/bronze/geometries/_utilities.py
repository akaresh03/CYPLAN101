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


def process_geometries(input_geojson_path, output_geoparquet_path):
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


def process_all_geometries(input_directory, output_directory):
    """
    Process all GeoJSON files in a directory to GeoParquet format.

    Parameters:
    -----------
    input_directory : str or Path
        Directory containing GeoJSON files
    output_directory : str or Path
        Directory to save GeoParquet files
    """
    input_dir = Path(input_directory)
    output_dir = Path(output_directory)

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process each GeoJSON file
    for filename in os.listdir(input_dir):
        if filename.endswith(".geojson"):
            # Clean the filename
            base_name = filename.replace(".geojson", "")
            cleaned_name = clean_name(base_name)

            # Set up paths
            input_path = input_dir / filename
            output_path = output_dir / f"{cleaned_name}.geoparquet"

            # Process the file
            process_geometries(input_path, output_path)
