import math
from count_distance import count_distance


# never got this to work well enough so i made
# fringe search so this will prob be deleted


def ida_star(graph, start, end):
    threshold = count_distance(graph, start, end)
    path = [start]

    while True:
        print('iteration with threshold: ' + str(threshold))
        t = ida_star_search(graph, end, 0, threshold, path)
        if t is True:
            print('found')
            print((path, t))
            return (path, t)
        if t == math.inf:
            path.append(end)
            print('not found')
            print((path, t))
            return (path, t)
        threshold = t


def ida_star_search(graph, end, distance, threshold, path):
    node = path[-1]
    estimate = distance + count_distance(graph, node, end)
    if estimate > threshold:
        return estimate

    if node == end:
        return True

    minium = math.inf
    for edge in edges(graph, node, end):
        neighbour = edge[0]
        edge_length = count_distance(graph, node, neighbour)

        if neighbour not in path:
            path.append(neighbour)
            temp = ida_star_search(
                graph, end, distance + edge_length, threshold, path)
            if temp is True:
                return True
            elif temp < minium:
                minium = temp
            path.pop()
    return minium


def edges(graph, node, end):
    estimates = []
    for edge in graph.edges(node):
        node = edge[1]
        h = count_distance(graph, node, end)
        estimates.append((node, h))
    estimates.sort(key=lambda a: a[1])
    return estimates
