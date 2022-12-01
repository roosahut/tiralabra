import unittest
from latlng_node_changes import change_node_route_to_latlng
from graph.graph import Graph
from tests.fakemultigraph import FakeMultiGraph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.multigraph = FakeMultiGraph()
        self.graph = Graph(self.multigraph)

    def test_function_turns_a_list_of_nodes_of_graph_to_right_latlng(self):
        route = change_node_route_to_latlng(self.graph, [1, 3, 5, 7])
        self.assertEqual(route, [[1, 1], [2, 1], [3, 1], [4, 1.5]])
