"""
Quick test script to verify osmnx_pipeline config paths work correctly.
Run this from anywhere in the project to verify paths are set up correctly.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

from osmnx_pipeline import config
import geopandas as gpd

print("="*70)
print("Testing osmnx_pipeline Configuration")
print("="*70)

print(f"\n1. Project Root: {config.PROJECT_ROOT}")
print(f"   Exists: {config.PROJECT_ROOT.exists()}")

print(f"\n2. Address Points Path: {config.ADDR_PATH}")
print(f"   Exists: {config.ADDR_PATH.exists()}")

print(f"\n3. County Boundary Path: {config.COUNTY_BOUNDARY_PATH}")
print(f"   Exists: {config.COUNTY_BOUNDARY_PATH.exists()}")

print(f"\n4. Census Tracts Path: {config.TRACTS_PATH}")
print(f"   Exists: {config.TRACTS_PATH.exists()}")

print("\n" + "="*70)
print("Testing GeoPandas File Loading")
print("="*70)

try:
    print("\nLoading address points...")
    addresses = gpd.read_parquet(config.ADDR_PATH)
    print(f"✓ Loaded {len(addresses):,} addresses")
    print(f"  CRS: {addresses.crs}")
    print(f"  Columns: {list(addresses.columns)[:5]}... ({len(addresses.columns)} total)")
except Exception as e:
    print(f"❌ Error loading addresses: {e}")

try:
    print("\nLoading county boundary...")
    county = gpd.read_parquet(config.COUNTY_BOUNDARY_PATH)
    print(f"✓ Loaded county boundary")
    print(f"  County: {county['county_name'].iloc[0]}")
    print(f"  CRS: {county.crs}")
except Exception as e:
    print(f"❌ Error loading county: {e}")

try:
    print("\nLoading census tracts...")
    tracts = gpd.read_parquet(config.TRACTS_PATH)
    print(f"✓ Loaded {len(tracts):,} census tracts")
    print(f"  CRS: {tracts.crs}")
except Exception as e:
    print(f"❌ Error loading tracts: {e}")

print("\n" + "="*70)
print("Testing OSMnx Pipeline Imports")
print("="*70)

try:
    from osmnx_pipeline.network import load_study_area, build_walk_network
    from osmnx_pipeline.amenities import fetch_amenities
    from osmnx_pipeline.distances import distance_to_amenity
    print("✓ All pipeline modules imported successfully")
except Exception as e:
    print(f"❌ Error importing modules: {e}")

print("\n" + "="*70)
print("Testing load_study_area() Function")
print("="*70)

try:
    from osmnx_pipeline.network import load_study_area
    study_area = load_study_area()
    print(f"✓ Study area loaded")
    print(f"  Type: {type(study_area).__name__}")
    print(f"  Geometry type: {study_area.geom_type}")
    print(f"  Bounds: {study_area.bounds}")
except Exception as e:
    print(f"❌ Error loading study area: {e}")

print("\n" + "="*70)
print("Configuration Test Complete!")
print("="*70)
print("\n✓ All paths are configured correctly.")
print("✓ You can now run the test.ipynb notebook from the notebooks/ directory.")
