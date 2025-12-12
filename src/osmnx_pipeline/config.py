from pathlib import Path

# Project root directory (go up from src/osmnx_pipeline to project root)
PROJECT_ROOT = Path(__file__).parent.parent.parent

CRS_LATLON = "EPSG:4326"
CRS_PROJECTED = "EPSG:26910"  # UTM zone 10N

OSM_TAGS_HIGH = {
    "bus_stops": {"highway": "bus_stop"},
    "schools": {"amenity": ["school", "kindergarten"]},
    "parks": {"leisure": "park"},
    "grocery_stores": {"shop": ["supermarket", "grocery"]},
    "pharmacies": {"amenity": "pharmacy"},
    # add more later
}

# Paths to gold geometry files (absolute paths)
ADDR_PATH = PROJECT_ROOT / "data" / "gold" / "geometries" / "address_points.geoparquet"
COUNTY_BOUNDARY_PATH = PROJECT_ROOT / "data" / "gold" / "geometries" / "county_boundary.geoparquet"
TRACTS_PATH = PROJECT_ROOT / "data" / "gold" / "geometries" / "census_tract_boundaries.geoparquet"