import sys
sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest

# Determine if two lists intersect (by reference) and return the intersecting node


def intersection(l1, l2):
    p = l1.head
    q = l2.head
    c1 = 0
    c2 = 0

    while p.next:
        p = p.next
        c1 += 1
    tail_l1 = p
    c1 += 1

    while q.next:
        q = q.next
        c2 += 1
    tail_l2 = q
    c2 += 1

    # No intersection if the ends are different
    if tail_l1 != tail_l2:
        return None

    if c1 > c2:
        p = l1.head
        q = l2.head
    else:
        p = l2.head
        q = l1.head

    delta = c1 - c2
    while delta > 0:
        p = p.next
        delta -= 1

    while p != q:
        p = p.next
        q = q.next

    return p

class Test(unittest.TestCase):
    def test_no_intersection(self):
        l1 = SLL.SinglyLinkedList()
        l2 = SLL.SinglyLinkedList()
        n11 = SLL.SinglyLinkedList.Node(1)
        n12 = SLL.SinglyLinkedList.Node(2)
        n13 = SLL.SinglyLinkedList.Node(3)

        n21 = SLL.SinglyLinkedList.Node(4)
        n22 = SLL.SinglyLinkedList.Node(5)
        n23 = SLL.SinglyLinkedList.Node(6)

        l1.head = n11
        n11.next = n12
        n12.next = n13

        l2.head = n21
        n21.next = n22
        n22.next = n23

        self.assertEqual(None, intersection(l1, l2))

    def test_intersection(self):
        l1 = SLL.SinglyLinkedList()
        l2 = SLL.SinglyLinkedList()
        n11 = SLL.SinglyLinkedList.Node(1)
        n12 = SLL.SinglyLinkedList.Node(2)
        n13 = SLL.SinglyLinkedList.Node(3)

        n21 = SLL.SinglyLinkedList.Node(4)
        n22 = SLL.SinglyLinkedList.Node(5)
        n23 = SLL.SinglyLinkedList.Node(6)

        l1.head = n11
        n11.next = n12
        n12.next = n13

        l2.head = n21
        n21.next = n12  # intersection

        self.assertEqual(n12, intersection(l1, l2))

    def test_intersection2(self):
        l1 = SLL.SinglyLinkedList()
        l2 = SLL.SinglyLinkedList()
        n11 = SLL.SinglyLinkedList.Node(1)
        n12 = SLL.SinglyLinkedList.Node(2)
        n13 = SLL.SinglyLinkedList.Node(3)

        n21 = SLL.SinglyLinkedList.Node(4)
        n22 = SLL.SinglyLinkedList.Node(5)
        n23 = SLL.SinglyLinkedList.Node(6)

        l1.head = n11
        n11.next = n12
        n12.next = n13

        l2.head = n11

        self.assertEqual(n11, intersection(l1, l2))

    def test_intersection3(self):
        l1 = SLL.SinglyLinkedList()
        l2 = SLL.SinglyLinkedList()
        n11 = SLL.SinglyLinkedList.Node(1)
        n12 = SLL.SinglyLinkedList.Node(2)
        n13 = SLL.SinglyLinkedList.Node(3)
        n14 = SLL.SinglyLinkedList.Node(4)

        n21 = SLL.SinglyLinkedList.Node(4)
        n22 = SLL.SinglyLinkedList.Node(5)
        n23 = SLL.SinglyLinkedList.Node(6)

        l1.head = n11
        n11.next = n12
        n12.next = n13
        n13.next = n14

        l2.head = n21
        n21.next = n13

        self.assertEqual(n13, intersection(l1, l2))


if __name__ == '__main__':
    unittest.main()
