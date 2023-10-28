import unittest
import sys

sys.path.insert(0, "../data_structures")
from BinaryTree import BinaryTree


# Given two nodes in a Binary Tree, find the common ancestor, if any

def covers(root, node):
    if not root:
        return False
    if root == node:
        return True
    return covers(root.left, node) or covers(root.right, node)


def first_common_ancestor_helper(root, p, q):
    if not root or root is p or root is q:
        return root
    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)
    if p_is_on_left != q_is_on_left:
        return root
    child = root.left if p_is_on_left else root.right
    return first_common_ancestor_helper(child, p, q)


def first_common_ancestor(root, p, q):
    if not covers(root, p) or not covers(root, q):
        return None
    return first_common_ancestor_helper(root, p, q)


class Test(unittest.TestCase):
    def test_1(self):
        tree = BinaryTree()
        n1 = tree.insert_left(7, tree.root)
        n2 = tree.insert_left(1, n1)
        n3 = tree.insert_right(9, n1)
        n4 = tree.insert_left(1, n2)
        n5 = tree.insert_right(3, n2)
        n6 = tree.insert_left(8, n3)
        n7 = tree.insert_right(15, n3)
        n8 = tree.insert_left(10, n7)
        n9 = tree.insert_right(19, n7)
        n10 = tree.insert_right(1, n9)

        self.assertEqual(n1, first_common_ancestor(tree.root, n1, n2))
        self.assertEqual(n1, first_common_ancestor(tree.root, n2, n3))
        self.assertEqual(n1, first_common_ancestor(tree.root, n3, n2))
        self.assertEqual(n2, first_common_ancestor(tree.root, n4, n5))
        self.assertEqual(n1, first_common_ancestor(tree.root, n4, n8))
        self.assertEqual(n7, first_common_ancestor(tree.root, n8, n10))
        self.assertEqual(n3, first_common_ancestor(tree.root, n9, n6))


if __name__ == '__main__':
    unittest.main()
