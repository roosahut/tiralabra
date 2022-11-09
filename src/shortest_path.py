import math
from math import radians, cos, sin, asin, sqrt
from queue import PriorityQueue

EARTH_RADIUS = 6371000


def dijkstra(graph, start, end):
    visited = set()

    costs = {n[0]: math.inf for n in graph.edges}
    paths = {n[0]: "" for n in graph.edges}
    costs[start] = 0
    paths[start] = str(start)

    pq = PriorityQueue()
    pq.put((costs[start], start))

    while not pq.empty():
        (length, node) = pq.get()

        if node in visited:
            continue
        visited.add(node)

        for edge in graph.edges(node):
            neighbour = edge[1]
            current_length = costs[neighbour]
            new_length = length + count_distance(graph, node, neighbour)

            if new_length < current_length:
                costs[neighbour] = new_length
                paths[neighbour] = paths[node] + \
                    " " + str(neighbour)
                pq.put((new_length, neighbour))

    return [int(n) for n in paths[end].strip().split(" ")]


def count_distance(graph, start, end):
    start_lon = radians(graph.nodes[start]['x'])
    end_lon = radians(graph.nodes[end]['x'])
    start_lat = radians(graph.nodes[start]['y'])
    end_lat = radians(graph.nodes[end]['y'])

    distance_lon = end_lon - start_lon
    distance_lat = end_lon - start_lat
    a = sin(distance_lat / 2)**2 + cos(start_lat) * \
        cos(end_lat) * sin(distance_lon / 2)**2
    b = 2 * asin(sqrt(a))
    # return the distance in meters
    return (b * EARTH_RADIUS)