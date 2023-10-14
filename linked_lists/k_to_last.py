import sys
sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest

# Return the kth to last element of a list


def k_to_last(sl, k):
    c = sl.count()
    steps = c - k - 1
    p = sl.head
    while steps > 0:
        p = p.next
        steps -= 1
    return p.value


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(4, k_to_last(SLL.SinglyLinkedList([1, 2, 3, 4]), 0))
        self.assertEqual(3, k_to_last(SLL.SinglyLinkedList([1, 2, 3, 4]), 1))
        self.assertEqual(2, k_to_last(SLL.SinglyLinkedList([1, 2, 3, 4]), 2))
        self.assertEqual(1, k_to_last(SLL.SinglyLinkedList([1, 2, 3, 4]), 3))


if __name__ == '__main__':
    unittest.main()
