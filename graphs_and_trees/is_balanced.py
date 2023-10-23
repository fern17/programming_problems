import unittest
import sys

sys.path.insert(0, "../data_structures")
from BinaryTree import BinaryTree


# Given a BinaryTree, write a function to check if the tree is balanced or not.
# A balanced tree is one in which the height of two subheights at the same level differs at most in one

NULL_VALUE = -10


def check_height(node):
    if not node:
        return -1
    hl = check_height(node.left)
    if hl == NULL_VALUE:
        return NULL_VALUE
    hr = check_height(node.right)
    if hr == NULL_VALUE:
        return NULL_VALUE
    if abs(hr - hl) > 1:
        return NULL_VALUE
    else:
        return max(hl, hr) + 1


def is_balanced(tree):
    return check_height(tree.root) != NULL_VALUE


class Test(unittest.TestCase):
    def test_1(self):
        tree = BinaryTree()
        self.assertEqual(True, is_balanced(tree))
        n1 = tree.insert_left(1, tree.root)
        self.assertEqual(True, is_balanced(tree))
        n2 = tree.insert_left(2, n1)
        n3 = tree.insert_right(3, n1)
        self.assertEqual(True, is_balanced(tree))
        n4 = tree.insert_left(4, n2)
        n5 = tree.insert_right(5, n2)
        n6 = tree.insert_left(6, n3)
        self.assertEqual(True, is_balanced(tree))
        n7 = tree.insert_left(7, n6)
        n8 = tree.insert_right(8, n6)
        self.assertEqual(False, is_balanced(tree))
        n9 = tree.insert_right(9, n8)
        self.assertEqual(False, is_balanced(tree))

    def test_2(self):
        tree = BinaryTree()
        self.assertEqual(True, is_balanced(tree))
        n1 = tree.insert_left(1, tree.root)
        self.assertEqual(True, is_balanced(tree))
        n2 = tree.insert_left(2, n1)
        self.assertEqual(True, is_balanced(tree))
        n3 = tree.insert_left(3, n2)
        self.assertEqual(False, is_balanced(tree))


if __name__ == '__main__':
    unittest.main()
