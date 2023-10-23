import unittest
import sys

sys.path.insert(0, "../data_structures")
from BinaryTree import BinaryTree


# Implement a function to check whether a BinaryTree is a BinarySearchTree

UNBOUNDED_VALUE = -10


def _is_bst(node, min_value, max_value):
    if not node:
        return True
    else:
        if min_value != UNBOUNDED_VALUE and node.value <= min_value:
            return False
        if max_value != UNBOUNDED_VALUE and node.value > max_value:
            return False

        c1 = _is_bst(node.left, min_value, node.value)
        c2 = _is_bst(node.right, node.value, max_value)
        if not c1 or not c2:
            return False
        else:
            return True


def is_bst(tree):
    return _is_bst(tree.root, UNBOUNDED_VALUE, UNBOUNDED_VALUE)


class Test(unittest.TestCase):
    def test_1(self):
        tree = BinaryTree()
        self.assertEqual(True, is_bst(tree))
        n1 = tree.insert_left(7, tree.root)
        self.assertEqual(True, is_bst(tree))
        n2 = tree.insert_left(1, n1)
        n3 = tree.insert_right(9, n1)
        self.assertEqual(True, is_bst(tree))
        n4 = tree.insert_left(1, n2)
        n5 = tree.insert_right(3, n2)
        self.assertEqual(True, is_bst(tree))
        n6 = tree.insert_left(8, n3)
        n7 = tree.insert_right(15, n3)
        n8 = tree.insert_left(10, n7)
        n9 = tree.insert_right(19, n7)
        self.assertEqual(True, is_bst(tree))
        n10 = tree.insert_right(1, n9)
        self.assertEqual(False, is_bst(tree))

    def test_2(self):
        tree = BinaryTree()
        self.assertEqual(True, is_bst(tree))
        n1 = tree.insert_left(3, tree.root)
        self.assertEqual(True, is_bst(tree))
        n2 = tree.insert_left(2, n1)
        self.assertEqual(True, is_bst(tree))
        n3 = tree.insert_right(1, n1)
        self.assertEqual(False, is_bst(tree))

    def test_3(self):
        tree = BinaryTree()
        n1 = tree.insert_left(3, tree.root)
        n2 = tree.insert_left(2, n1)
        n3 = tree.insert_right(1, n2)
        n3 = tree.insert_right(7, n2)
        self.assertEqual(False, is_bst(tree))


if __name__ == '__main__':
    unittest.main()
