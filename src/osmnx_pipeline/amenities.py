import osmnx as ox
from .config import CRS_LATLON, CRS_PROJECTED, OSM_TAGS_HIGH
from .network import load_study_area
import geopandas as gpd

def fetch_amenities(amenity_key: str) -> gpd.GeoDataFrame:
    tags = OSM_TAGS_HIGH[amenity_key]
    poly_ll = load_study_area()
    gdf = ox.features_from_polygon(poly_ll, tags=tags)
    gdf = gdf.to_crs(CRS_PROJECTED)
    return gdf[gdf.geometry.type == "Point"]