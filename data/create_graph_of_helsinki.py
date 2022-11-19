import osmnx as ox
import pickle

# i used this to load the graph of helsinki
# that is currently in the helsinki_graph.pickle

place = 'Helsinki, Finland'
G = ox.graph_from_place(
    place, network_type='walk', simplify=True)


pickle.dump(G, open('helsinki_graph.pickle', 'wb'))
