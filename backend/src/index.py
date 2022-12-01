import pickle
import osmnx as ox
from graph.graph import Graph
from algorithms.dijkstra import dijkstra
from algorithms.fringe_search import fringe_search
from latlng_node_changes import change_node_route_to_latlng


def get_shortest_path(start, end):
    G = pickle.load(open('./backend/data/helsinki_graph.pickle', 'rb'))
    graph = Graph(G)

    start_node = get_openstreetmap_node_from_latlng(G, start)
    end_node = get_openstreetmap_node_from_latlng(G, end)

    (path_fringe, cost_fringe) = fringe_search(graph, start_node, end_node)
    (path_dijkstra, cost_dijkstra) = dijkstra(graph, start_node, end_node)
    print(f'fringe search cost: {cost_fringe}')
    print(f'dijkstra cost: {cost_dijkstra}')

    fringe_in_latlng = change_node_route_to_latlng(graph, path_fringe)
    dijkstra_inlatlng = change_node_route_to_latlng(graph, path_dijkstra)

    return fringe_in_latlng, dijkstra_inlatlng


def get_openstreetmap_node_from_latlng(graph, position):
    node = ox.nearest_nodes(graph, position[1], position[0])
    return node

#G = pickle.load(open('data/helsinki_graph.pickle', 'rb'))

#start = (60.184136, 24.949670)
#end = (60.186760, 24.978402)

#start_node = get_openstreetmap_node_from_latlng(G, start)
#end_node = get_openstreetmap_node_from_latlng(G, end)

#graph = Graph(G)

#print(dijkstra(graph, start_node, end_node))

#print(fringe_search(graph, start_node, end_node))
#print(ida_star(G, start_node, end_node))

#graph = Graph(G)

#print(ida_star(G, start_node, end_node))

# Shows the graph with osmnx
# fig, ax = ox.plot_graph(G, node_color='red', node_size=15,
#                        node_zorder=2, node_edgecolor='k')

# Shows the route and graph with osmnx
#shortest_route_map = ox.plot_graph_route(G, my_dijstra)
# shortest_route_map

# Shows the map and the route with folium and then creates a html file that can be opened
#shortest_route_map = ox.plot_route_folium(G, shortest_path)
# shortest_route_map.save('route.html')
