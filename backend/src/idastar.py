import math
from count_distance import count_distance

# this doesnt work yet :D


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
