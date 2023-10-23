import unittest
import sys
sys.path.insert(0, "../data_structures")
from BinaryTree import BinaryTree

# Given a BinaryTree, return a list of lists. Each list i contains the nodes at level i


def list_of_depths(tree):
    nodes_per_level = []
    if not tree.root:
        return []
    bfs_queue = [(tree.root, 0)]
    while bfs_queue:
        (node, level) = bfs_queue.pop(0)
        if len(nodes_per_level) == level:
            nodes_per_level.append([])
        nodes_per_level[level].append(node.value)
        if node.left:
            bfs_queue.append((node.left, level + 1))
        if node.right:
            bfs_queue.append((node.right, level + 1))
    return nodes_per_level


class Test(unittest.TestCase):
    def test_1(self):
        tree = BinaryTree()
        self.assertEqual([], list_of_depths(tree))
        n1 = tree.insert_left(1, tree.root)
        self.assertEqual([[1]], list_of_depths(tree))
        n2 = tree.insert_left(2, n1)
        n3 = tree.insert_right(3, n1)
        self.assertEqual([[1], [2, 3]], list_of_depths(tree))
        n4 = tree.insert_left(4, n2)
        n5 = tree.insert_right(5, n2)
        n6 = tree.insert_left(6, n3)
        self.assertEqual([[1], [2, 3], [4, 5, 6]], list_of_depths(tree))
        n7 = tree.insert_left(7, n6)
        n8 = tree.insert_right(8, n6)
        self.assertEqual([[1], [2, 3], [4, 5, 6], [7, 8]], list_of_depths(tree))
        n9 = tree.insert_right(9, n8)
        self.assertEqual([[1], [2, 3], [4, 5, 6], [7, 8], [9]], list_of_depths(tree))

    def test_2(self):
        tree = BinaryTree()
        self.assertEqual([], list_of_depths(tree))
        n1 = tree.insert_left(1, tree.root)
        self.assertEqual([[1]], list_of_depths(tree))
        n2 = tree.insert_left(2, n1)
        self.assertEqual([[1], [2]], list_of_depths(tree))
        n3 = tree.insert_left(3, n2)
        self.assertEqual([[1], [2], [3]], list_of_depths(tree))
        n4 = tree.insert_left(4, n3)
        self.assertEqual([[1], [2], [3], [4]], list_of_depths(tree))
        n5 = tree.insert_left(5, n4)
        self.assertEqual([[1], [2], [3], [4], [5]], list_of_depths(tree))
        n6 = tree.insert_left(6, n5)
        self.assertEqual([[1], [2], [3], [4], [5], [6]], list_of_depths(tree))
        n7 = tree.insert_left(7, n6)
        self.assertEqual([[1], [2], [3], [4], [5], [6], [7]], list_of_depths(tree))
        n8 = tree.insert_left(8, n7)
        self.assertEqual([[1], [2], [3], [4], [5], [6], [7], [8]], list_of_depths(tree))
        n9 = tree.insert_left(9, n8)
        self.assertEqual([[1], [2], [3], [4], [5], [6], [7], [8], [9]], list_of_depths(tree))


if __name__ == '__main__':
    unittest.main()
