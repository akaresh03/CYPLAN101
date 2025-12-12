"""
Process address points from silver to gold layer with column renaming.
"""

from pathlib import Path
import geopandas as gpd


def process():
    """Process address points data with clean column names."""
    print("\nProcessing: Address Points")

    # Load from silver
    script_dir = Path(__file__).parent.parent.parent.parent
    silver_path = script_dir / "data" / "silver" / "geometries" / "address_points.geoparquet"

    print(f"  Loading from silver...")
    gdf = gpd.read_parquet(silver_path)
    print(f"    → Loaded {len(gdf)} features")

    # Column mapping: old names → clean names
    column_mapping = {
        'APN': 'parcel_number',
        'ST_NUM': 'street_number',
        'FEANME': 'street_name',
        'FEATYP': 'street_type',
        'DIRPRE': 'direction_prefix',
        'DIRSUF': 'direction_suffix',
        'MUN': 'municipality',
        'UNIT': 'unit_number',
        'UNIT_TYP': 'unit_type',
        'SRC_DATE': 'source_date',
        'REV_DATE': 'revision_date',
        'SPADID': 'address_point_id',
        'ADDRESS': 'full_address',
        'CITY': 'city',
        'ZIPCODE': 'zipcode',
        'ADDRESSLOOKUP': 'address_lookup',
        'X_CORD': 'x_coordinate',
        'Y_CORD': 'y_coordinate',
        'geometry': 'geometry'
    }

    # Rename columns (only rename columns that exist)
    columns_to_rename = {old: new for old, new in column_mapping.items() if old in gdf.columns}
    gdf = gdf.rename(columns=columns_to_rename)
    print(f"    → Renamed {len(columns_to_rename)} columns")

    # Save to gold
    gold_dir = script_dir / "data" / "gold" / "geometries"
    gold_dir.mkdir(parents=True, exist_ok=True)
    gold_path = gold_dir / "address_points.geoparquet"

    gdf.to_parquet(gold_path, compression='snappy', index=False)
    print(f"    → Saved to gold: {gold_path.name}")

    print("  ✓ Address Points complete\n")


if __name__ == "__main__":
    process()
