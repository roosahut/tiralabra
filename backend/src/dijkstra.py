import heapq
import math


def dijkstra(graph, start, end):
    visited = set()

    costs = {node: math.inf for node in graph.nodes}
    paths = {node: "" for node in graph.nodes}
    costs[start] = 0
    paths[start] = str(start)

    min_dist = [(costs[start], start)]

    while min_dist:
        (length, node) = heapq.heappop(min_dist)

        if node in visited:
            continue
        visited.add(node)

        node_object = graph.nodes[node]
        for edge in node_object.neighbours:
            # print(edge)
            neighbour = edge['id']
            current_length = costs[neighbour]
            new_length = length + edge['length']

            if new_length < current_length:
                costs[neighbour] = new_length
                paths[neighbour] = paths[node] + \
                    " " + str(neighbour)
                heapq.heappush(min_dist, (new_length, neighbour))

    return ([int(n) for n in paths[end].strip().split(" ")], costs[end])
