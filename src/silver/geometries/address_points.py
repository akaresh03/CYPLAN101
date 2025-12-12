"""
Process address points from bronze to silver layer.
"""

from _utilities import process_geometry


def process():
    """Process address points data."""
    print("\nProcessing: Address Points")

    # Load bronze data
    # gdf = ("Address_Points_5658052068094417558.geojson")

    # TODO: Add any address-points-specific transformations here
    # For now, just pass through the data

    # Save to silver
    process_geometry("Address_Points_5658052068094417558.geojson", "bronze", "silver")

    print("  ✓ Address Points complete\n")


if __name__ == "__main__":
    process()
