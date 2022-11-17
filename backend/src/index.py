import osmnx as ox
from shortest_path import dijkstra, ida_star

address = 'Hämeentie 33, Helsinki, Finland'
G = ox.graph_from_address(
    address, network_type='walk', dist=2000, simplify=False)

# Shows the graph with osmnx
# fig, ax = ox.plot_graph(G, node_color='red', node_size=15,
# node_zorder=2, node_edgecolor='k')

# the church of kallio
start = (60.184136, 24.949670)

# shopping centre redi
end = (60.186760, 24.978402)

start_node = ox.nearest_nodes(G, start[1], start[0])
end_node = ox.nearest_nodes(G, end[1], end[0])

#print(start_node, end_node)

(shortest_path, cost) = dijkstra(G, start_node, end_node)
print(cost)

route_in_lonlat = []
for node in shortest_path:
    x = G.nodes[node]['x']
    y = G.nodes[node]['y']
    pos = [y, x]
    route_in_lonlat.append(pos)

print(route_in_lonlat)

#print(ida_star(G, start_node, end_node))

# Shows the route and graph with osmnx
#shortest_route_map = ox.plot_graph_route(G, my_dijstra)
# shortest_route_map

# Shows the map and the route with folium and then creates a html file that can be opened
shortest_route_map = ox.plot_route_folium(G, shortest_path)
shortest_route_map.save('route.html')
