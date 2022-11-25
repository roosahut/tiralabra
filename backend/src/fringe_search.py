import math
from count_distance import count_distance


def fringe_search(graph, start, end):
    fringe = [start]
    cache = {n: None for n in graph.nodes}
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
                break
            for edge in edges(graph, node, end):
                child = edge[0]
                g_child = g + count_distance(graph, node, child)
                # print(cache)
                # print(cache[child])
                if cache[child] != None:
                    (g_cached, parent) = cache[child]
                    if g_child >= g_cached:
                        continue
                # print(child)
                # print(fringe)
                if len(fringe) > 0:
                    if child in fringe:
                        fringe.remove(child)
                fringe = insert_child_after_node(fringe, node, child)
                cache[child] = (g_child, node)
            fringe.remove(node)
        flimit = fmin

    if found == True:
        path = []
        reverse_path(cache, end, path)
        return path
    else:
        return False


def reverse_path(cache, node, path):
    (g, parent) = cache[node]
    if parent != None:
        reverse_path(cache, parent, path)
    path.append(node)


def insert_child_after_node(fringe, node, child):
    # print(fringe)
    #print(f'node: {node} child: {child}')
    for i in range(len(fringe)):
        if fringe[i] == node:
            index = i + 1
            if index == len(fringe):
                fringe.append(child)
            else:
                fringe.insert(index, child)
            break
    #print(f'new fringe: {fringe}')
    return fringe


def edges(graph, node, end):
    estimates = []
    for edge in graph.edges(node):
        node = edge[1]
        h = count_distance(graph, node, end)
        estimates.append((node, h))
    estimates.sort(key=lambda a: a[1])
    # print(estimates)
    return estimates
