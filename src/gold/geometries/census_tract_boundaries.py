"""
Process census tract boundaries from silver to gold layer with column renaming.
"""

from pathlib import Path
import geopandas as gpd


def process():
    """Process census tract boundaries data with clean column names."""
    print("\nProcessing: Census Tract Boundaries")

    # Load from silver
    script_dir = Path(__file__).parent.parent.parent.parent
    silver_path = script_dir / "data" / "silver" / "geometries" / "census_tract_boundaries.geoparquet"

    print(f"  Loading from silver...")
    gdf = gpd.read_parquet(silver_path)
    print(f"    → Loaded {len(gdf)} features")

    # Column mapping
    column_mapping = {
        'OBJECTID': 'id',
        'DIST_NAME': 'tract_name',
        'DISTRICT_ID': 'tract_id',
        'geometry': 'geometry'
    }

    # Rename columns (only rename columns that exist)
    columns_to_rename = {old: new for old, new in column_mapping.items() if old in gdf.columns}
    gdf = gdf.rename(columns=columns_to_rename)
    print(f"    → Renamed {len(columns_to_rename)} columns")

    # Save to gold
    gold_dir = script_dir / "data" / "gold" / "geometries"
    gold_dir.mkdir(parents=True, exist_ok=True)
    gold_path = gold_dir / "census_tract_boundaries.geoparquet"

    gdf.to_parquet(gold_path, compression='snappy', index=False)
    print(f"    → Saved to gold: {gold_path.name}")

    print("  ✓ Census Tract Boundaries complete\n")


if __name__ == "__main__":
    process()
