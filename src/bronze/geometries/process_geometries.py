"""
Convert GeoJSON files to GeoParquet format (Bronze Layer).

This script should only be run once to process the geometry files.
"""

from pathlib import Path
from _utilities import process_all_geometries


def main():
    """Convert all GeoJSON files to GeoParquet."""
    # Get project root directory
    script_dir = Path(__file__).parent.parent.parent.parent  # Up to attempt-2/
    input_directory = script_dir / "data" / "bronze" / "geometries"
    output_directory = script_dir / "data" / "bronze" / "geometries"

    print("="*60)
    print("BRONZE LAYER: CONVERTING GEOJSON TO GEOPARQUET")
    print("="*60)
    print(f"Input: {input_directory}")
    print(f"Output: {output_directory}\n")

    process_all_geometries(input_directory, output_directory)

    print("\n✓ All files converted successfully!")
    print("\nNext step: Run silver layer processing")
    print("  cd ../../silver/geometries")
    print("  python process_geometries.py")


if __name__ == "__main__":
    main()
