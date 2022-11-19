import osmnx as ox


def get_openstreetmap_node_from_latlng(graph, position):
    node = ox.nearest_nodes(graph, position[1], position[0])
    return node


def change_node_route_to_latlng(graph, route):
    route_in_lanlng = []
    for node in route:
        x = graph.nodes[node]['x']
        y = graph.nodes[node]['y']
        position = [y, x]
        route_in_lanlng.append(position)
    return route_in_lanlng
