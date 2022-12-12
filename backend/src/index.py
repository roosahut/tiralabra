import pickle
import osmnx as ox
from graph.graph import Graph
from algorithms.dijkstra import dijkstra
from algorithms.fringe_search import fringe_search
from latlng_node_changes import change_node_route_to_latlng


def get_shortest_path(start, end):
    """The function that gives the api the route based on the given start and
    end points.

    Args:
        start (tuple): Latitude and longitude of the start point.
        end (tuple): Latitude and longitude of the end point.

    Returns:
        Two lists of the routes calculated by dijkstra and fringe search.
    """
    G = pickle.load(open('./backend/data/helsinki_graph.pickle', 'rb'))
    graph = Graph(G)

    start_node = get_openstreetmap_node_from_latlng(G, start)
    end_node = get_openstreetmap_node_from_latlng(G, end)

    (path_fringe, cost_fringe) = fringe_search(graph, start_node, end_node)
    (path_dijkstra, cost_dijkstra) = dijkstra(graph, start_node, end_node)
    print(f'fringe search cost: {cost_fringe}')
    print(f'dijkstra cost: {cost_dijkstra}')

    fringe_in_latlng = change_node_route_to_latlng(graph, path_fringe)
    dijkstra_inlatlng = change_node_route_to_latlng(graph, path_dijkstra)

    return fringe_in_latlng, dijkstra_inlatlng


def get_openstreetmap_node_from_latlng(graph, position):
    """Uses osmnx to find the closest nodes in the graph
    to the latitude and longitude of the start and end points.

    Args:
        graph (_networkx.MultiGraph_): The graph that osmnx uses to find the nodes from.
        position (tuple): The latitude and longitude of the wanted point.

    Returns:
        The closest node in the graph.
    """
    node = ox.nearest_nodes(graph, position[1], position[0])
    return node
