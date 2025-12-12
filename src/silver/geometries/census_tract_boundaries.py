"""
Process census tract boundaries from bronze to silver layer.
"""

from _utilities import process_geometry


def process():
    """Process census tract boundaries data."""
    print("\nProcessing: Census Tract Boundaries")

    # Convert from bronze GeoJSON to silver geoparquet
    process_geometry("Census_Tract_Boundaries_7506545346012929933.geojson", "bronze", "silver")

    print("  ✓ Census Tract Boundaries complete\n")


if __name__ == "__main__":
    process()
