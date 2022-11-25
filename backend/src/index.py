import pickle
from dijkstra import dijkstra
from latlng_node_changes import get_openstreetmap_node_from_latlng, change_node_route_to_latlng
from graph import Graph
from idastar import ida_star
from fringe_search import fringe_search


def get_shortest_path(start, end):
    G = pickle.load(open('data/helsinki_graph.pickle', 'rb'))

    start_node = get_openstreetmap_node_from_latlng(G, start)
    end_node = get_openstreetmap_node_from_latlng(G, end)

    path_fringe = fringe_search(G, start_node, end_node)
    (path_dijkstra, cost) = dijkstra(G, start_node, end_node)
    # print(cost)

    fringe_in_latlng = change_node_route_to_latlng(G, path_fringe)
    dijkstra_inlatlng = change_node_route_to_latlng(G, path_dijkstra)
    # print(route_in_latlng)

    return fringe_in_latlng, dijkstra_inlatlng


#G = pickle.load(open('data/helsinki_graph.pickle', 'rb'))

#start = (60.184136, 24.949670)
#end = (60.186760, 24.978402)

#start_node = get_openstreetmap_node_from_latlng(G, start)
#end_node = get_openstreetmap_node_from_latlng(G, end)

#print(fringe_search(G, start_node, end_node))
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
