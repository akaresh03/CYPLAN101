"""
Process county boundary from bronze to silver layer.
"""

from _utilities import process_geometry


def process():
    """Process county boundary data."""
    print("\nProcessing: County Boundary")

    # Convert from bronze GeoJSON to silver geoparquet
    process_geometry("County_Boundary_-7887526420565696345.geojson", "bronze", "silver")

    print("  ✓ County Boundary complete\n")


if __name__ == "__main__":
    process()
