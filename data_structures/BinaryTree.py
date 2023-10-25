import unittest
import SinglyLinkedList as SLL


class BinaryTree:
    class Node:
        def __init__(self, v, parent=None):
            self.value = v
            self.left = None
            self.right = None
            self.parent = parent

    def __init__(self):
        self.root = None

    def insert_left(self, v, parent):
        new_node = self.Node(v, parent)
        if parent is None:
            self.root = new_node
        else:
            parent.left = new_node
        return new_node

    def insert_right(self, v, parent):
        new_node = self.Node(v, parent)
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

    # assumes BST
    def successor(self, node):
        if not node:
            return None
        if node.right:
            candidate = node.right
            while candidate.left:
                candidate = candidate.left
            return candidate
        else:
            q = node
            candidate = q.parent
            while candidate and candidate.left is not q:
                q = candidate
                candidate = candidate.parent
            return candidate


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

    def test_successor(self):
        tree = BinaryTree()
        self.assertEqual(None, tree.successor(None))
        n1 = tree.insert_left(7, tree.root)
        self.assertEqual(None, tree.successor(n1))
        n2 = tree.insert_left(1, n1)
        self.assertEqual(n1, tree.successor(n2))
        n3 = tree.insert_right(9, n1)
        self.assertEqual(None, tree.successor(n3))
        n4 = tree.insert_left(1, n2)
        self.assertEqual(n2, tree.successor(n4))
        n5 = tree.insert_right(3, n2)
        self.assertEqual(n1, tree.successor(n5))
        n6 = tree.insert_left(8, n3)
        n7 = tree.insert_right(15, n3)
        n8 = tree.insert_left(10, n7)
        n9 = tree.insert_right(19, n7)
        self.assertEqual(n6, tree.successor(n1))
        self.assertEqual(n5, tree.successor(n2))
        self.assertEqual(n8, tree.successor(n3))
        self.assertEqual(n2, tree.successor(n4))
        self.assertEqual(n1, tree.successor(n5))
        self.assertEqual(n3, tree.successor(n6))
        self.assertEqual(n9, tree.successor(n7))
        self.assertEqual(n7, tree.successor(n8))
        self.assertEqual(None, tree.successor(n9))


if __name__ == '__main__':
    unittest.main()
