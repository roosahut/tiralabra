import unittest
from algorithms.fringe_search import fringe_search
from graph.graph import Graph
from tests.fakemultigraph import FakeMultiGraph


class TestFringeSearch(unittest.TestCase):
    def setUp(self):
        self.multigraph = FakeMultiGraph()
        self.graph = Graph(self.multigraph)

    def test_fringe_search_returns_the_right_route(self):
        start_node = 1
        end_node = 7
        (route, cost, time) = fringe_search(self.graph, start_node, end_node)
        self.assertEqual(route, [1, 3, 5, 7])

    def test_fringe_search_returns_the_rigth_cost(self):
        start_node = 1
        end_node = 6
        (route, cost, time) = fringe_search(self.graph, start_node, end_node)
        self.assertEqual(cost, 3)

    def test_fringe_returns_the_right_route_two(self):
        start_node = 4
        end_node = 8
        (route, cost, time) = fringe_search(self.graph, start_node, end_node)
        self.assertEqual(route, [4, 6, 7, 8])

    def test_fringe_returns_the_rigth_cost_two(self):
        start_node = 4
        end_node = 8
        (route, cost, time) = fringe_search(self.graph, start_node, end_node)
        self.assertEqual(cost, 2.5)
