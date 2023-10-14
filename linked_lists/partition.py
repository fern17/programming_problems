import sys
sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest

# Partition a list around an element of value v, so that the elements
# whose value is below v appear before the elements whose value is bigger than v


def partition(l, v):
    below = []
    above = []
    p = l.head
    while p:
        if p.value <= v:
            below.append(p.value)
        else:
            above.append(p.value)
        p = p.next
    merged_lists = below + above
    return merged_lists


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([3, 1, 2, 5, 4], partition(SLL.SinglyLinkedList([5, 4, 3, 1, 2]), 3))
        self.assertEqual([1, 5, 4, 3, 2], partition(SLL.SinglyLinkedList([5, 4, 3, 1, 2]), 1))
        self.assertEqual([4, 3, 1, 2, 5], partition(SLL.SinglyLinkedList([5, 4, 3, 1, 2]), 4))
        self.assertEqual([3, 5, 5, 2, 1, 8, 10], partition(SLL.SinglyLinkedList([3, 5, 8, 5, 10, 2, 1]), 5))


if __name__ == '__main__':
    unittest.main()
