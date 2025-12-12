"""
Process street centerlines from bronze to silver layer.
"""

from _utilities import process_geometry


def process():
    """Process street centerlines data."""
    print("\nProcessing: Street Centerlines")

    # Convert from bronze GeoJSON to silver geoparquet
    process_geometry("Street_Centerlines_-8203296818607454791.geojson", "bronze", "silver")

    print("  ✓ Street Centerlines complete\n")


if __name__ == "__main__":
    process()
