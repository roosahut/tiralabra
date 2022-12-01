def change_node_route_to_latlng(graph, route):
    """Changes the route with nodes to the latitude and 
    longitude points.

    Args:
        graph (object): The Graph class.
        route (list): A list of nodes.

    Returns:
        A list of the route in lattitude and longitude.
    """
    route_in_lanlng = []
    for node in route:
        x = graph.nodes[node].position[0]
        y = graph.nodes[node].position[1]
        position = [x, y]
        route_in_lanlng.append(position)
    return route_in_lanlng
