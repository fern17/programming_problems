import sys
sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest

# Remove duplicates from a Single Linked List


def remove_duplicates(l):
    if l.is_empty():
        return l
    p = l.head
    while p is not None:
        q = p.next
        while q is not None:
            if p.value == q.value:
                q = l.remove_node(q)
            q = q.next
        p = p.next
    return l


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3], remove_duplicates(SLL.SinglyLinkedList([1, 2, 3])).as_list())
        self.assertEqual([1, 2], remove_duplicates(SLL.SinglyLinkedList([1, 2, 2])).as_list())
        self.assertEqual([1, 2, 3], remove_duplicates(SLL.SinglyLinkedList([1, 2, 2, 3, 3, 3])).as_list())
        self.assertEqual([2, 1, 3], remove_duplicates(SLL.SinglyLinkedList([2, 1, 3, 2])).as_list())


if __name__ == '__main__':
    unittest.main()
