import heapq
import math
from src.count_distance import count_distance


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
