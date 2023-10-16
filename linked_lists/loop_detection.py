import sys
sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest

import unittest

# Given a linked list which might contain a loop, return the node of the beginning of the loop (if any)


def loop_detection_v1(l):
    nodes = set()
    p = l.head
    while p:
        if p in nodes:
            return p
        nodes.add(p)
        p = p.next
    return None

def loop_detection_v2(l):
    slower = l.head
    faster = l.head
    while faster and faster.next:
        slower = slower.next
        faster = faster.next.next
        if slower == faster:
            break
    if not slower or not faster or not faster.next:
        return None
    slower = l.head
    while slower != faster:
        slower = slower.next
        faster = faster.next
    return slower


class Test(unittest.TestCase):

    def test_no_loop(self):
        l = SLL.SinglyLinkedList()
        n11 = SLL.SinglyLinkedList.Node(1)
        n12 = SLL.SinglyLinkedList.Node(2)
        n13 = SLL.SinglyLinkedList.Node(3)

        l.head = n11
        n11.next = n12
        n12.next = n13

        self.assertEqual(None, loop_detection_v1(l))
        self.assertEqual(None, loop_detection_v2(l))

    def test_loop_1(self):
        l = SLL.SinglyLinkedList()
        n11 = SLL.SinglyLinkedList.Node(1)
        n12 = SLL.SinglyLinkedList.Node(2)
        n13 = SLL.SinglyLinkedList.Node(3)

        l.head = n11
        n11.next = n12
        n12.next = n13
        n13.next = n12

        self.assertEqual(n12, loop_detection_v1(l))
        self.assertEqual(n12, loop_detection_v2(l))

    def test_loop_2(self):
        l = SLL.SinglyLinkedList()
        n11 = SLL.SinglyLinkedList.Node(1)
        n12 = SLL.SinglyLinkedList.Node(2)
        n13 = SLL.SinglyLinkedList.Node(3)

        l.head = n11
        n11.next = n12
        n12.next = n13
        n13.next = n11

        self.assertEqual(n11, loop_detection_v1(l))
        self.assertEqual(n11, loop_detection_v2(l))


if __name__ == '__main__':
    unittest.main()
