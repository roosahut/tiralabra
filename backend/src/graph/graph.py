from graph.node import Node


class Graph:
    """Changes the Networkx MultiGraph osmnx gives from the OpenStreetMap to a simpler graph
        so the algorithms can be in simpler forms and testing will be easier.
    """

    def __init__(self, G):
        """The constructor.

        Args:
            G (networkx.MultiGraph): The graph osmnx takes from
            OpenStreetMap of Helsinki (stored in data dictionary).
        """
        self.nodes = self.create_nodes(G)

    def create_nodes(self, G):
        """Creates    else: the nodes for the Graph object.

        Args:
            G (networkx.MultiGraph): Same as in constructor

        Returns:
            Return a dictionary with the node ids as keys and the Node objects as values.
        """
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
