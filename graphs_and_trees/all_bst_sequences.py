import unittest
import sys

sys.path.insert(0, "../data_structures")
from BinaryTree import BinaryTree


# Given a BST, find all the possible array sequences that could have generated it

def mix_lists(first_list, second_list, result_lists, prefix):
    if not first_list or not second_list:
        r = prefix.copy()
        r.extend(first_list)
        r.extend(second_list)
        result_lists.append(r)
        return
    hf = first_list.pop(0)
    prefix.append(hf)
    mix_lists(first_list, second_list, result_lists, prefix)
    prefix.pop()
    first_list.insert(0, hf)

    hs = second_list.pop(0)
    prefix.append(hs)
    mix_lists(first_list, second_list, result_lists, prefix)
    prefix.pop()
    second_list.insert(0, hs)


def all_possible_sequences(node):
    result_lists = []
    if not node:
        result_lists.append([])
        return result_lists
    else:
        prefix = [node.value]
        lists_left = all_possible_sequences(node.left)
        lists_right = all_possible_sequences(node.right)
        for list_in_left in lists_left:
            for list_in_right in lists_right:
                mix = []
                mix_lists(list_in_left, list_in_right, mix, prefix)
                result_lists.extend(mix)
        return result_lists


class Test(unittest.TestCase):
    def test_1(self):
        tree = BinaryTree()
        n1 = tree.insert_left(7, tree.root)
        self.assertEqual([[7]], all_possible_sequences(tree.root))
        n2 = tree.insert_left(2, n1)
        self.assertEqual([[7, 2]], all_possible_sequences(tree.root))
        n3 = tree.insert_right(9, n1)
        self.assertEqual([[7, 2, 9], [7, 9, 2]], all_possible_sequences(tree.root))
        n4 = tree.insert_left(1, n2)
        n5 = tree.insert_right(3, n2)
        n6 = tree.insert_left(8, n3)
        n7 = tree.insert_right(15, n3)
        n8 = tree.insert_left(10, n7)
        n9 = tree.insert_right(19, n7)
        n10 = tree.insert_right(1, n9)

        print(all_possible_sequences(tree.root))


if __name__ == '__main__':
    unittest.main()
