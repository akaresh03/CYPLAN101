"""
Process county boundary from silver to gold layer with column renaming.
"""

from pathlib import Path
import geopandas as gpd


def process():
    """Process county boundary data with clean column names."""
    print("\nProcessing: County Boundary")

    # Load from silver
    script_dir = Path(__file__).parent.parent.parent.parent
    silver_path = script_dir / "data" / "silver" / "geometries" / "county_boundary.geoparquet"

    print(f"  Loading from silver...")
    gdf = gpd.read_parquet(silver_path)
    print(f"    → Loaded {len(gdf)} features")

    # Column mapping
    column_mapping = {
        'OBJECTID': 'id',
        'NAME': 'county_name',
        'Shape_STArea_1': 'area_sqm',
        'Shape_STLength_1': 'perimeter_m',
        'geometry': 'geometry'
    }

    # Rename columns (only rename columns that exist)
    columns_to_rename = {old: new for old, new in column_mapping.items() if old in gdf.columns}
    gdf = gdf.rename(columns=columns_to_rename)
    print(f"    → Renamed {len(columns_to_rename)} columns")

    # Save to gold
    gold_dir = script_dir / "data" / "gold" / "geometries"
    gold_dir.mkdir(parents=True, exist_ok=True)
    gold_path = gold_dir / "county_boundary.geoparquet"

    gdf.to_parquet(gold_path, compression='snappy', index=False)
    print(f"    → Saved to gold: {gold_path.name}")

    print("  ✓ County Boundary complete\n")


if __name__ == "__main__":
    process()
