import osmnx as ox
from algorithms.dijkstra import dijkstra
from algorithms.fringe_search import fringe_search
from latlng_node_changes import change_node_route_to_latlng


def get_shortest_path(start, end, graph, G):
    """The function that gives the api the route based on the given start and
    end points.

    Args:
        start (tuple): Latitude and longitude of the start point.
        end (tuple): Latitude and longitude of the end point.
        graph (object): The graph of Helsinki in the graph object.
        G (Networkx.MultiGraph): The multigraph osmnx gives from OpenStreetMap.

    Returns:
        Both algorithms routes, costs and time it took them.
    """
    start_node = get_openstreetmap_node_from_latlng(G, start)
    end_node = get_openstreetmap_node_from_latlng(G, end)

    (path_fringe, cost_fringe, time_fringe) = fringe_search(
        graph, start_node, end_node)
    (path_dijkstra, cost_dijkstra, time_dijkstra) = dijkstra(
        graph, start_node, end_node)
    print(f'fringe search cost: {cost_fringe}')
    print(f'fringe search time: {time_fringe}')
    print(f'dijkstra cost: {cost_dijkstra}')
    print(f'dijkstra time: {time_dijkstra}')

    fringe_in_latlng = change_node_route_to_latlng(graph, path_fringe)
    dijkstra_inlatlng = change_node_route_to_latlng(graph, path_dijkstra)

    return {'fringe':
            {'route': fringe_in_latlng, 'cost': round(
                cost_fringe, 2), 'time': round(time_fringe, 7)},
            'dijkstra':
            {'route': dijkstra_inlatlng, 'cost': round(cost_dijkstra, 2), 'time': round(time_dijkstra, 7)}}


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
