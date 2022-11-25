import math
from count_distance import count_distance
from queue import PriorityQueue
from heapq import heappush, heappop

# this doesnt work yet :D


def ida_star(graph, start, end):
    threshold = count_distance(graph, start, end)
    path = [start]

    #paths = deque()
    #paths.append((0, [path]))
    # visited.add(start)

    while True:
        #path = paths.pop()
        print('iteration with threshold: ' + str(threshold))
        # print(f'{path}')
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
    #print('visiting node: ' + str(node))
    #print(count_distance(graph, node, end))
    estimate = distance + count_distance(graph, node, end)
    #print(f'estimate: {estimate}')
    if estimate > threshold:
        #paths.append(estimate, path)
        #print('new estimate: ' + str(estimate))
        #print('estimate was smaller than threshold')
        return estimate

    if node == end:
        return True

    minium = math.inf
    for edge in edges(graph, node, end):
        #print(f'min: {minium}')
        neighbour = edge[0]
        edge_length = count_distance(graph, node, neighbour)

        if neighbour not in path:
            path.append(neighbour)
            # print(path)
            temp = ida_star_search(
                graph, end, distance + edge_length, threshold, path)
            #print(f'temp: {temp}')
            if temp is True:
                return True
            elif temp < minium:
                #print('temp was smaller than min')
                minium = temp
            path.pop()
    #print(f'return current min: {minium}')
    return minium


def edges(graph, node, end):
    estimates = []
    for edge in graph.edges(node):
        node = edge[1]
        h = count_distance(graph, node, end)
        estimates.append((node, h))
    estimates.sort(key=lambda a: a[1])
    # print(estimates)
    return estimates


def a_star(graph, start, end):
    to_visit = PriorityQueue()
    to_visit.put(start)

    while not to_visit.empty():
        node = to_visit.get()
        if node == end:
            return end
        for edge in graph.edges(node):
            neighbour = edge[1]
