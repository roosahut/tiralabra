import math
from math import radians, cos, sin, asin, sqrt
import heapq
from collections import deque

from typing import Deque


EARTH_RADIUS = 6371000


def dijkstra(graph, start, end):
    visited = set()

    costs = {n[0]: math.inf for n in graph.edges}
    paths = {n[0]: "" for n in graph.edges}
    costs[start] = 0
    paths[start] = str(start)

    min_dist = [(costs[start], start)]

    while min_dist:
        (length, node) = heapq.heappop(min_dist)

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
                heapq.heappush(min_dist, (new_length, neighbour))

    return ([int(n) for n in paths[end].strip().split(" ")], costs[end])


def count_distance(graph, start, end):
    start_lon = radians(graph.nodes[start]['x'])
    end_lon = radians(graph.nodes[end]['x'])
    start_lat = radians(graph.nodes[start]['y'])
    end_lat = radians(graph.nodes[end]['y'])

    distance_lon = end_lon - start_lon
    distance_lat = end_lat - start_lat
    a = sin(distance_lat / 2)**2 + cos(start_lat) * \
        cos(end_lat) * sin(distance_lon / 2)**2
    b = 2 * asin(sqrt(a))
    # return the distance in meters
    return (b * EARTH_RADIUS)

# in ida* the count_distance is the heuristic function because
# it counts the shortest distance between two points on a map


def ida_star(graph, start, end):
    threshold = count_distance(graph, start, end)
    path = []
    path.append(start)

    #paths = deque()
    #paths.append((0, [path]))
    # visited.add(start)

    while True:
        #path = paths.pop()
        print('iteration with threshold: ' + str(threshold))
        t = ida_star_search(graph, start, end, 0, threshold, path)
        if t < 0:
            return -1
        elif t == math.inf:
            return -1
        else:
            threshold = t


def ida_star_search(graph, start, end, distance, threshold, path):
    node = path[-1]
    #print('visiting node: ' + str(node))
    #print(count_distance(graph, node, end))
    estimate = distance + count_distance(graph, node, end)
    if estimate > threshold:
        #paths.append(estimate, path)
        #print('new estimate: ' + str(estimate))
        return estimate

    if node == end:
        return -distance

    minium = math.inf
    for edge in graph.edges(node):
        neighbour = edge[1]
        edge_length = count_distance(graph, node, neighbour)

        if neighbour not in path:
            new_distance = distance + edge_length
            if count_distance(graph, start, neighbour) <= new_distance:
                continue
            path.append(neighbour)
            temp = ida_star_search(
                graph, start, end, new_distance, threshold, path)
            if temp < 0:
                return temp
            elif temp < minium:
                minium = temp
            path.pop()

    return minium
