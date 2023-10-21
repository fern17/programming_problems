import unittest
import SinglyLinkedList as SLL


class BinaryTree:
    class Node:
        def __init__(self, v):
            self.value = v
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_left(self, v, parent):
        new_node = self.Node(v)
        if parent is None:
            self.root = new_node
        else:
            parent.left = new_node
        return new_node

    def insert_right(self, v, parent):
        new_node = self.Node(v)
        if parent is None:
            self.root = new_node
        else:
            parent.right = new_node
        return new_node

    def bfs(self):
        nodes = []
        if self.root:
            nodes_queue = [self.root]
            while nodes_queue:
                current_node = nodes_queue.pop(0)
                if current_node:
                    nodes.append(current_node.value)
                    nodes_queue.append(current_node.left)
                    nodes_queue.append(current_node.right)
        return nodes

    def dfs(self):
        nodes = []
        if self.root:
            nodes_stack = [self.root]
            while nodes_stack:
                current_node = nodes_stack.pop()
                if current_node:
                    nodes.append(current_node.value)
                    if current_node.right:
                        nodes_stack.append(current_node.right)
                    if current_node.left:
                        nodes_stack.append(current_node.left)
        return nodes


class Test(unittest.TestCase):
    def test_basic(self):
        tree = BinaryTree()

        self.assertEqual([], tree.bfs())
        self.assertEqual([], tree.dfs())

        n1 = tree.insert_left(1, tree.root)
        n2 = tree.insert_left(2, n1)
        n3 = tree.insert_right(3, n1)

        self.assertEqual([1, 2, 3], tree.bfs())
        self.assertEqual([1, 2, 3], tree.dfs())

        tree.insert_left(4, n2)
        self.assertEqual([1, 2, 3, 4], tree.bfs())
        self.assertEqual([1, 2, 4, 3], tree.dfs())

        tree.insert_right(5, n2)
        n6 = tree.insert_left(6, n3)
        self.assertEqual([1, 2, 3, 4, 5, 6], tree.bfs())
        self.assertEqual([1, 2, 4, 5, 3, 6], tree.dfs())

        tree.insert_left(7, n6)
        n8 = tree.insert_right(8, n6)
        tree.insert_right(9, n8)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], tree.bfs())
        self.assertEqual([1, 2, 4, 5, 3, 6, 7, 8, 9], tree.dfs())


if __name__ == '__main__':
    unittest.main()
