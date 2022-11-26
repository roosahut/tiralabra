import math
from count_distance import count_distance


def fringe_search(graph, start, end):
    fringe = [start]
    cache = {node: None for node in graph.nodes}
    cache[start] = (0, None)
    flimit = count_distance(graph, start, end)
    found = False

    while found == False and len(fringe) > 0:
        fmin = math.inf
        for node in fringe:
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
                if cache[child] != None:
                    (g_cached, parent) = cache[child]
                    if g_child >= g_cached:
                        continue
                if child in fringe:
                    fringe.remove(child)
                fringe = insert_child_after_node(fringe, node, child)
                cache[child] = (g_child, node)
            fringe.remove(node)
        flimit = fmin

    if found == True:
        path = []
        reverse_path(cache, end, path)
        return path, cost
    else:
        return False


def reverse_path(cache, node, path):
    (g, parent) = cache[node]
    if parent != None:
        reverse_path(cache, parent, path)
    path.append(node)


def insert_child_after_node(fringe, node, child):
    for i in range(len(fringe)):
        if fringe[i] == node:
            index = i + 1
            fringe.insert(index, child)
            break
    return fringe


def sort_edges(graph, node_object, end):
    estimates = []
    for edge in node_object.neighbours:
        neighbour = edge['id']
        length_to_node = edge['length']
        h = count_distance(graph, neighbour, end)
        estimates.append((neighbour, h, length_to_node))
    estimates.sort(key=lambda a: a[1])
    return estimates
