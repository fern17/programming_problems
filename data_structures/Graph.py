import collections
import unittest


class Graph:
    def __init__(self, number_nodes, directed):
        self.number_nodes = number_nodes
        self.adjacencies = [[0] * self.number_nodes for _ in range(self.number_nodes)]
        self.directed = directed

    def add_edge(self, src, dst, weight=1):
        if src < self.number_nodes and dst < self.number_nodes:
            self.adjacencies[src][dst] = weight
            if not self.directed:
                self.adjacencies[dst][src] = weight

    def neighbors(self, i):
        n_i = []
        if i < self.number_nodes:
            li = self.adjacencies[i]
            for j in range(len(li)):
                if li[j] != 0:
                    n_i.append(j)
        return n_i

    def neighbors_with_weights(self, i):
        n_i = []
        if i < self.number_nodes:
            li = self.adjacencies[i]
            for j in range(len(li)):
                if li[j] != 0:
                    n_i.append((j, li[j]))
        return n_i

    def bfs(self, start_node=0):
        if self.number_nodes == 0 or start_node >= self.number_nodes:
            return []
        visited = [False] * self.number_nodes
        nodes = []
        visit_queue = [start_node]
        while len(visit_queue) > 0:
            next_node = visit_queue.pop(0)
            if not visited[next_node]:
                nodes.append(next_node)
                visited[next_node] = True
                n_n = self.neighbors(next_node)
                for i in n_n:
                    if not visited[i]:
                        visit_queue.append(i)
        return nodes

    def dfs(self, start_node=0):
        if self.number_nodes == 0 or start_node >= self.number_nodes:
            return []
        visited = [False] * self.number_nodes
        nodes = []
        visit_stack = [start_node]
        while len(visit_stack) > 0:
            next_node = visit_stack.pop(0)
            if not visited[next_node]:
                nodes.append(next_node)
                visited[next_node] = True
                n_n = self.neighbors(next_node)
                new_to_visit = []
                for i in n_n:
                    if not visited[i]:
                        new_to_visit.append(i)
                visit_stack = new_to_visit + visit_stack
        return nodes

    def topological_sort(self):
        def find_next(adj):
            if not adj:
                return -1
            best_value = -1
            best_key = -1
            for k, v in adj.items():
                n = len(v)
                if best_value == -1 or (best_value != -1 and n < best_value):
                    best_value = n
                    best_key = k
            return best_key

        adjacencies = collections.OrderedDict()
        for i in range(self.number_nodes):
            adjacencies[i] = self.neighbors(i)
        nodes = []
        n = find_next(adjacencies)
        while n in adjacencies:
            nodes.append(n)
            adjacencies.pop(n)
            for k, v in adjacencies.items():
                if n in v:
                    v.remove(n)
            n = find_next(adjacencies)
        return nodes

    def print(self, with_weights=False):
        for i in range(self.number_nodes):
            n_i = self.neighbors_with_weights(i) if with_weights else self.neighbors(i)
            print(f'{i} -> {n_i}')


class Test(unittest.TestCase):
    def test_directed(self):
        graph = Graph(3, directed=True)
        assert [] == graph.neighbors(0)
        assert [] == graph.neighbors(1)
        graph.add_edge(0, 1)
        assert [1] == graph.neighbors(0)
        assert [] == graph.neighbors(1)
        graph.add_edge(0, 2)
        assert [1, 2] == graph.neighbors(0)
        assert [] == graph.neighbors(2)
        graph.add_edge(1, 2)
        assert [1, 2] == graph.neighbors(0)
        assert [2] == graph.neighbors(1)
        assert [] == graph.neighbors(2)

        assert [0, 1, 2] == graph.bfs()
        assert [0, 1, 2] == graph.dfs()

    def test_undirected(self):
        graph = Graph(4, directed=False)
        assert [] == graph.neighbors(0)
        assert [] == graph.neighbors(1)
        graph.add_edge(0, 1)
        assert [1] == graph.neighbors(0)
        assert [0] == graph.neighbors(1)
        graph.add_edge(0, 2)
        assert [1, 2] == graph.neighbors(0)
        assert [0] == graph.neighbors(2)
        graph.add_edge(1, 2)
        assert [1, 2] == graph.neighbors(0)
        assert [0, 2] == graph.neighbors(1)
        assert [0, 1] == graph.neighbors(2)

    def test_directed_with_weight(self):
        graph = Graph(3, directed=True)
        graph.add_edge(0, 1, 3)
        assert [(1, 3)] == graph.neighbors_with_weights(0)
        assert [] == graph.neighbors_with_weights(1)
        graph.add_edge(0, 2, 1)
        assert [(1, 3), (2, 1)] == graph.neighbors_with_weights(0)
        assert [] == graph.neighbors_with_weights(1)
        assert [] == graph.neighbors_with_weights(2)
        graph.add_edge(1, 2, 5)
        assert [(1, 3), (2, 1)] == graph.neighbors_with_weights(0)
        assert [(2, 5)] == graph.neighbors_with_weights(1)
        assert [] == graph.neighbors_with_weights(2)

    def test_undirected_with_weight(self):
        graph = Graph(3, directed=False)
        graph.add_edge(0, 1, 3)
        assert [(1, 3)] == graph.neighbors_with_weights(0)
        assert [(0, 3)] == graph.neighbors_with_weights(1)
        graph.add_edge(0, 2, 1)
        assert [(1, 3), (2, 1)] == graph.neighbors_with_weights(0)
        assert [(0, 3)] == graph.neighbors_with_weights(1)
        assert [(0, 1)] == graph.neighbors_with_weights(2)
        graph.add_edge(1, 2, 5)
        assert [(1, 3), (2, 1)] == graph.neighbors_with_weights(0)
        assert [(0, 3), (2, 5)] == graph.neighbors_with_weights(1)
        assert [(0, 1), (1, 5)] == graph.neighbors_with_weights(2)

    def test_search(self):
        graph = Graph(7, directed=False)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 4)
        graph.add_edge(3, 5)
        graph.add_edge(4, 6)
        graph.add_edge(5, 6)
        assert [1, 2] == graph.neighbors(0)
        assert [0, 3, 4] == graph.neighbors(1)
        assert [0, 4] == graph.neighbors(2)
        assert [1, 5] == graph.neighbors(3)
        assert [1, 2, 6] == graph.neighbors(4)
        assert [3, 6] == graph.neighbors(5)
        assert [4, 5] == graph.neighbors(6)

        assert [0, 1, 2, 3, 4, 5, 6] == graph.bfs()
        assert [0, 1, 2, 3, 4, 5, 6] == graph.bfs(0)
        assert [1, 0, 3, 4, 2, 5, 6] == graph.bfs(1)
        assert [6, 4, 5, 1, 2, 3, 0] == graph.bfs(6)
        assert [0, 1, 3, 5, 6, 4, 2] == graph.dfs()
        assert [0, 1, 3, 5, 6, 4, 2] == graph.dfs(0)
        assert [1, 0, 2, 4, 6, 5, 3] == graph.dfs(1)
        assert [6, 4, 1, 0, 2, 3, 5] == graph.dfs(6)

    def test_topological_sort(self):
        graph = Graph(9, directed=True)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], graph.topological_sort())
        graph.add_edge(1, 5)
        graph.add_edge(2, 1)
        graph.add_edge(2, 5)
        graph.add_edge(2, 8)
        graph.add_edge(3, 1)
        graph.add_edge(4, 7)
        graph.add_edge(6, 1)
        graph.add_edge(6, 3)
        graph.add_edge(6, 2)
        self.assertEqual([0, 5, 1, 3, 7, 4, 8, 2, 6], graph.topological_sort())


if __name__ == '__main__':
    unittest.main()
