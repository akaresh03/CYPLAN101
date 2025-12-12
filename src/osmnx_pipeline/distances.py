import osmnx as ox
import networkx as nx
import geopandas as gpd
from .config import CRS_PROJECTED, ADDR_PATH
from .network import build_walk_network
from .amenities import fetch_amenities

def distance_to_amenity(amenity_key: str) -> gpd.GeoDataFrame:
    # load data
    addresses = gpd.read_parquet(ADDR_PATH).to_crs(CRS_PROJECTED)
    G = build_walk_network()
    amenities = fetch_amenities(amenity_key)

    # snap to nodes
    addr_nodes = ox.nearest_nodes(
        G,
        addresses.geometry.x.values,
        addresses.geometry.y.values,
    )
    amen_nodes = ox.nearest_nodes(
        G,
        amenities.geometry.x.values,
        amenities.geometry.y.values,
    )
    addresses["nearest_node"] = addr_nodes
    amenities["nearest_node"] = amen_nodes

    # multi-source dijkstra
    dest_nodes = amenities["nearest_node"].unique().tolist()
    lengths = nx.multi_source_dijkstra_path_length(
        G, dest_nodes, weight="length"
    )

    col = f"dist_{amenity_key}_m"
    addresses[col] = addresses["nearest_node"].map(lengths)
    return addresses


