# changing the networkx multi graph osmnx gives
# from openstreetmap to a simpler graph to
# help testing etc.

# this one is still in progress

class Graph:
    def __init__(self, G):
        self.nodes = self.create_nodes(G)
        self.edges = self.create_edges(G)

    def create_nodes(self, G):
        # print(G.nodes)
        pass

    def create_edges(self, G):
        pass
