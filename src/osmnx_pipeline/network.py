import osmnx as ox
import geopandas as gpd
from .config import CRS_LATLON, CRS_PROJECTED, COUNTY_BOUNDARY_PATH

def load_study_area():
    boundary = gpd.read_parquet(COUNTY_BOUNDARY_PATH)
    boundary_ll = boundary.to_crs(CRS_LATLON)
    return boundary_ll.geometry.iloc[0]

def build_walk_network():
    poly_ll = load_study_area()
    G = ox.graph_from_polygon(poly_ll, network_type="walk")
    G_proj = ox.project_graph(G, to_crs=CRS_PROJECTED)
    return G_proj