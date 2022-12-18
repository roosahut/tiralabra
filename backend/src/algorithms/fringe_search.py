import math
from math import radians, cos, sin, asin, sqrt
from timeit import default_timer as timer

EARTH_RADIUS = 6371000


def fringe_search(graph, start, end):
    """ The path-finding fringe search algorithm.

    Args:
        graph (object): The Graph object that was created from the Networkx graph.
        start (int): Start node.
        end (int): End node.

    Returns:
        Returns a tuple where there is the calculated route and the cost in meters.
    """
    start_time = timer()

    fringe = [start]
    cache = {node: None for node in graph.nodes}
    cache[start] = (0, None)
    flimit = count_distance(graph, start, end)
    found = False
    visited_nodes = 0

    while found is False and len(fringe) > 0:
        fmin = math.inf
        for node in fringe:
            visited_nodes += 1
            (g, parent) = cache[node]
            f = g + count_distance(graph, node, end)
            if f > flimit:
                fmin = min(f, fmin)
                continue
            if node == end:
                found = True
                cost = g
                break
            node_object = graph.nodes[node]
            for edge in sort_edges(graph, node_object, end):
                child = edge[0]
                g_child = g + edge[2]
                if cache[child] is not None:
                    (g_cached, parent) = cache[child]
                    if g_child >= g_cached:
                        continue
                if child in fringe:
                    fringe.remove(child)
                fringe = insert_child_after_node(fringe, node, child)
                cache[child] = (g_child, node)
            fringe.remove(node)
        flimit = fmin

    if found is True:
        path = []
        reverse_path(cache, end, path)
        print(f'fringe visited nodes: {visited_nodes}')
        return (path, cost, timer() - start_time)
    return False


def reverse_path(cache, node, path):
    """Reverses the path of the fringe search from it's cache.

    Args:
        cache (dict): The cache that was created when fringe search calculated the route.
        node (int): The current node.
        path (list): The counted route that this function builds.
    """
    (g, parent) = cache[node]
    if parent is not None:
        reverse_path(cache, parent, path)
    path.append(node)


def insert_child_after_node(fringe, node, child):
    """Inserts the child node after the parent node in the fringe.

    Args:
        fringe (list): The fringe of the fringe search.
        node (int): Current node.
        child (int): The child of the current node.

    Returns:
        The fringe with the child node after the parent node.
    """
    for i in range(len(fringe)):
        if fringe[i] == node:
            index = i + 1
            fringe.insert(index, child)
            break
    return fringe


def sort_edges(graph, node_object, end):
    """Sorts the edges of the given node based on the heuristic
    between the neighbour node and end node.

    Args:
        graph (object): The Graph object that was created from the Networkx graph.
        node_object (object): The current Node object whom edges are sorted
        end (int): The end node.

    Returns:
        A list of (neighbour_node, heuristic_to_end, length_between_neighbour_and_current)
        values sorted by the smallest heuristic to end.
    """
    estimates = []
    for edge in node_object.neighbours:
        neighbour = edge['id']
        length_to_node = edge['length']
        h = count_distance(graph, neighbour, end)
        estimates.append((neighbour, h, length_to_node))
    estimates.sort(key=lambda a: a[1])
    return estimates


def count_distance(graph, start, end):
    """The heuristic function that counts the straight line distance between two nodes
    using the latitude and longitude of the nodes and maths to count distance
    on earth between two given points.

    Args:
        graph (object): The Graph object that was created from the Networkx graph.
        start (int): The start node.
        end (int): The end node.

    Returns:
        The distance between the nodes in meters.
    """
    start_object = graph.nodes[start]
    end_object = graph.nodes[end]

    start_lng = radians(start_object.position[1])
    end_lng = radians(end_object.position[1])
    start_lat = radians(start_object.position[0])
    end_lat = radians(end_object.position[0])

    distance_lon = end_lng - start_lng
    distance_lat = end_lat - start_lat
    a = sin(distance_lat / 2)**2 + cos(start_lat) * \
        cos(end_lat) * sin(distance_lon / 2)**2
    b = 2 * asin(sqrt(a))
    # return the distance in meters
    return (round(b * EARTH_RADIUS, 3))
