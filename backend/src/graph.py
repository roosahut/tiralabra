from node import Node

# changing the networkx multi graph osmnx gives
# from openstreetmap to a simpler graph to
# help testing etc.


class Graph:
    def __init__(self, G):
        self.nodes = self.create_nodes(G)

    def create_nodes(self, G):
        nodes = {}
        for node in G.nodes:
            lat = G.nodes[node]['y']
            lng = G.nodes[node]['x']

            neighbours = []
            for edge in list(G.edges(node, data=True)):
                neighbour = {'id': edge[1], 'length': edge[2]['length']}
                neighbours.append(neighbour)

            node_object = Node(node, (lat, lng), neighbours)
            nodes[node] = node_object

        return nodes
