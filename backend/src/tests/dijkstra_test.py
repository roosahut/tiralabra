import unittest
from algorithms.dijkstra import dijkstra
from graph.graph import Graph
from tests.fakemultigraph import FakeMultiGraph


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.multigraph = FakeMultiGraph()
        self.graph = Graph(self.multigraph)

    def test_dijkstra_returns_the_right_route_one(self):
        start_node = 1
        end_node = 7
        (route, cost, time) = dijkstra(self.graph, start_node, end_node)
        self.assertEqual(route, [1, 3, 5, 7])

    def test_dijkstra_returns_the_rigth_cost_one(self):
        start_node = 1
        end_node = 6
        (route, cost, time) = dijkstra(self.graph, start_node, end_node)
        self.assertEqual(cost, 3)

    def test_dijkstra_returns_the_right_route_two(self):
        start_node = 6
        end_node = 8
        (route, cost, time) = dijkstra(self.graph, start_node, end_node)
        self.assertEqual(route, [6, 7, 8])

    def test_dijkstra_returns_the_rigth_cost_two(self):
        start_node = 6
        end_node = 8
        (route, cost, time) = dijkstra(self.graph, start_node, end_node)
        self.assertEqual(cost, 1.5)
