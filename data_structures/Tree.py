import unittest
import SinglyLinkedList as SLL


class Tree:
    class Node:
        def __init__(self, v):
            self.value = v
            self.children = []

    def __init__(self):
        self.root = None

    def insert(self, v, parent):
        new_node = self.Node(v)
        if parent is None:
            self.root = new_node
        else:
            parent.children.append(new_node)
        return new_node


    def bfs(self):
        nodes = []
        if not self.root:
            return nodes
        queue = SLL.SinglyLinkedList()
        queue.push_back(self.root)
        while not queue.is_empty():
            p = queue.head
            nodes.append(p.value.value)
            queue.pop_front()
            for i in p.value.children:
                queue.push_back(i)
        return nodes

    def dfs(self):
        nodes = []
        if not self.root:
            return nodes
        stack = SLL.SinglyLinkedList()
        stack.push_back(self.root)
        visited = set()
        while not stack.is_empty():
            p = stack.head
            stack.pop_front()
            if p.value not in visited:
                nodes.append(p.value.value)
                visited.add(p.value)
                for i in reversed(p.value.children):
                    stack.push_front(i)
        return nodes



class Test(unittest.TestCase):
    def test_basic(self):
        tree = Tree()

        self.assertEqual([], tree.bfs())
        self.assertEqual([], tree.dfs())

        n1 = tree.insert(1, tree.root)
        n2 = tree.insert(2, n1)
        n3 = tree.insert(3, n1)

        self.assertEqual([1, 2, 3], tree.bfs())
        self.assertEqual([1, 2, 3], tree.dfs())

        tree.insert(4, n2)
        self.assertEqual([1, 2, 3, 4], tree.bfs())
        self.assertEqual([1, 2, 4, 3], tree.dfs())

        tree.insert(5, n2)
        tree.insert(6, n2)
        self.assertEqual([1, 2, 3, 4, 5, 6], tree.bfs())
        self.assertEqual([1, 2, 4, 5, 6, 3], tree.dfs())

        tree.insert(7, n3)
        n8 = tree.insert(8, n3)
        tree.insert(9, n8)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], tree.bfs())
        self.assertEqual([1, 2, 4, 5, 6, 3, 7, 8, 9], tree.dfs())


if __name__ == '__main__':
    unittest.main()
