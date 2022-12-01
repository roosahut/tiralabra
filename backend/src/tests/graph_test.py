import unittest
from graph.graph import Graph
from tests.fakemultigraph import FakeMultiGraph


class TestGraph(unittest.TestCase):
    def test_graph_creates_a_dict_of_nodes(self):
        MultiGraph = FakeMultiGraph()
        graph = Graph(MultiGraph)
        assert type(graph.nodes) is dict

    def test_graph_nodes_have_objects_as_values(self):
        MultiGraph = FakeMultiGraph()
        graph = Graph(MultiGraph)
        first_node = graph.nodes[1]
        self.assertEqual(first_node.position, (1, 1))
