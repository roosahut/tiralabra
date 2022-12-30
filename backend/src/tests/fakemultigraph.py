class FakeMultiGraph:
    """Creating a fake version of the Networkx MultiGraph so the class Graph can be tested.
    """

    def __init__(self):
        self.nodes = {1: {'y': 1, 'x': 1, 'neighbours': [[None, 2, {'length': 1}], [None, 3, {'length': 1}]]}, 2: {'y': 1, 'x': 2, 'neighbours': [[None, 1, {'length': 1}], [None, 4, {'length': 1}]]},
                      3: {'y': 2, 'x': 1, 'neighbours': [[None, 1, {'length': 1}], [None, 4, {'length': 1}], [None, 5, {'length': 1}]]}, 4: {'y': 2, 'x': 2, 'neighbours': [[None, 2, {'length': 1}], [None, 3, {'length': 1}], [None, 6, {'length': 1}]]},
                      5: {'y': 3, 'x': 1, 'neighbours': [[None, 2, {'length': 1}], [None, 6, {'length': 1}], [None, 7, {'length': 1}]]}, 6: {'y': 3, 'x': 2, 'neighbours': [[None, 4, {'length': 1}], [None, 5, {'length': 1}], [None, 7, {'length': 1}]]},
                      7: {'y': 4, 'x': 1.5, 'neighbours': [[None, 5, {'length': 1}], [None, 6, {'length': 1}], [None, 8, {'length': 0.5}]]}, 8: {'y': 4, 'x': 2, 'neighbours': [[None, 7, {'length': 0.5}]]}
                      }

    def edges(self, node, data):
        return self.nodes[node]['neighbours']
