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

    def _bfs(self, node):
        nodes = []
        if node:
            if node.left:
                nodes.append(node.left.value)
            if node.right:
                nodes.append(node.right.value)
            nodes.extend(self._bfs(node.left))
            nodes.extend(self._bfs(node.right))
        return nodes

    def bfs(self):
        nodes = []
        if self.root:
            nodes = [self.root.value]
            nodes.extend(self._bfs(self.root))
        return nodes

    def _dfs(self, stack):
        nodes = []
        while stack.head:
            p = stack.head.value
            stack.pop_front()
            if p and p.value:
                nodes.append(p.value)
                if p.right:
                    stack.push_front(p.right)
                if p.left:
                    stack.push_front(p.left)

        return nodes

    def dfs(self):
        stack = SLL.SinglyLinkedList([self.root])
        return self._dfs(stack)


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
