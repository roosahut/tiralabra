import heapq
import math
from timeit import default_timer as timer


def dijkstra(graph, start, end):
    """The dijkstra path-finding algorithm.

    Args:
        graph (object): The Graph object that was created from the Networkx graph.
        start (int): Start node.
        end (int): End node.

    Returns:
        Returns the calculated route, the cost in meters and the time 
        the algorithm took finding the route.
    """
    start_time = timer()

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
            neighbour = edge['id']
            current_length = costs[neighbour]
            new_length = length + edge['length']

            if new_length < current_length:
                costs[neighbour] = new_length
                paths[neighbour] = paths[node] + \
                    " " + str(neighbour)
                heapq.heappush(min_dist, (new_length, neighbour))

    print(f'dijkstras visited nodes: {len(visited)}')

    return ([int(n) for n in paths[end].strip().split(" ")], costs[end], timer() - start_time)
