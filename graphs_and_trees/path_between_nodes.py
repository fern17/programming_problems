import unittest
import sys
sys.path.insert(0, "../data_structures")
from Graph import Graph

# Given a directed graph, create a function to detect if there is a path between them


def are_connected(graph, src, dst):
    l = graph.dfs(src)
    return dst in l


class Test(unittest.TestCase):
    def test(self):
        graph = Graph(5, directed=True)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        self.assertEqual(True, are_connected(graph,0, 1))
        self.assertEqual(True, are_connected(graph, 0, 2))
        self.assertEqual(True, are_connected(graph, 0, 3))
        self.assertEqual(False, are_connected(graph, 0, 4))
        self.assertEqual(False, are_connected(graph, 4, 0))
        self.assertEqual(False, are_connected(graph, 3, 2))
        self.assertEqual(False, are_connected(graph, 3, 0))
        graph.add_edge(3, 4)
        self.assertEqual(True, are_connected(graph, 0, 4))



if __name__ == '__main__':
    unittest.main()
