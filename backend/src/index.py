import pickle
from src.dijkstra import dijkstra
from src.latlng_node_changes import get_openstreetmap_node_from_latlng, change_node_route_to_latlng


def get_shortest_path(start, end):
    G = pickle.load(open('data/helsinki_graph.pickle', 'rb'))

    start_node = get_openstreetmap_node_from_latlng(G, start)
    end_node = get_openstreetmap_node_from_latlng(G, end)

    (shortest_path, cost) = dijkstra(G, start_node, end_node)
    print(cost)

    route_in_latlng = change_node_route_to_latlng(G, shortest_path)
    # print(route_in_latlng)

    return route_in_latlng

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
