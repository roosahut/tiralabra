# changing the networkx multi graph osmnx gives
# from openstreetmap to a simpler graph to
# help testing etc.

# this one is still in progress
from node import Node


class Graph:
    def __init__(self, G):
        self.nodes = self.create_nodes(G)
        self.edges_length = self.get_edges_length(G)

    def create_nodes(self, G):
        nodes = []
        for node in G.nodes:
            lat = G.nodes[node]['y']
            lng = G.nodes[node]['x']
            #print(list(G.edges(node, data=True)))
            neighbours = []
            for edge in list(G.edges(node, data=True)):
                neighbour = {'id': edge[1], 'length': edge[2]['length']}
                neighbours.append(neighbour)
            node = Node(id, (lat, lng), neighbours)
            nodes.append(node)

    def get_edges_length(self, G):
        length = len(G.edges)
        print(length)
        return length
