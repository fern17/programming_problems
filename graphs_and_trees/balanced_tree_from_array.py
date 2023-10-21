import unittest
import sys
sys.path.insert(0, "../data_structures")
from BinaryTree import BinaryTree

# Given a sorted list of integers, create a binary search tree whose height is minimum


def fill_tree_helper(root, values):
    if not values:
        return None
    mid_idx = int(len(values) / 2)
    v = values.pop(mid_idx)
    root = BinaryTree.Node(v)
    root.left = fill_tree_helper(root.left, values[0:mid_idx])
    root.right = fill_tree_helper(root.right, values[mid_idx:])
    return root


def fill_tree(values):
    tree = BinaryTree()
    tree.root = fill_tree_helper(tree.root, values)
    return tree


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([], fill_tree([]).bfs())
        self.assertEqual([1], fill_tree([1]).bfs())
        self.assertEqual([2, 1, 3], fill_tree([1, 2, 3]).bfs())
        self.assertEqual([4, 2, 6, 1, 3, 5, 7], fill_tree([1, 2, 3, 4, 5, 6, 7]).bfs())
        self.assertEqual([3, 2, 4, 1], fill_tree([1, 2, 3, 4]).bfs())
        self.assertEqual([5, 3, 7, 2, 4, 6, 8, 1], fill_tree([1, 2, 3, 4, 5, 6, 7, 8]).bfs())



if __name__ == '__main__':
    unittest.main()
