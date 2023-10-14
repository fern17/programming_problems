import unittest


class SinglyLinkedList:
    class Node:
        def __init__(self, v):
            self.value = v
            self.next = None

    def __init__(self, initial_values=None):
        self.head = None
        if initial_values:
            for i in initial_values:
                self.push_back(i)

    def __eq__(self, other):
        p = self.head
        q = other.head
        while p and q and p.value == q.value:
            p = p.next
            q = q.next
        return p is None and q is None

    def is_empty(self):
        return self.head is None

    def count(self):
        c = 0
        p = self.head
        while p:
            p = p.next
            c += 1
        return c

    def as_list(self):
        l = []
        p = self.head
        while p:
            l.append(p.value)
            p = p.next
        return l

    def push_back(self, v):
        new_node = self.Node(v)
        if self.head:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
        else:
            self.head = new_node

    def pop_back(self):
        if not self.head:
            return None
        if not self.head.next:
            v = self.head.value
            self.head = None
            return v

        p = self.head
        q = self.head.next
        while q.next:
            p = p.next
            q = q.next
        v = q.value
        p.next = None
        return v

    def remove_node(self, n):
        if not self.head or not n:
            return None
        if self.head is n:
            self.head = self.head.next
            return self.head
        p = self.head
        while p and p.next is not n:
            p = p.next
        if p and p.next is n:
            p.next = n.next
            return p
        return None



class Test(unittest.TestCase):
    def test(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(True, linked_list.is_empty())
        self.assertEqual(0, linked_list.count())
        self.assertEqual([], linked_list.as_list())
        linked_list.push_back(1)
        self.assertEqual(1, linked_list.count())
        self.assertEqual([1], linked_list.as_list())
        self.assertEqual(False, linked_list.is_empty())
        linked_list.push_back(2)
        self.assertEqual([1, 2], linked_list.as_list())
        self.assertEqual(2, linked_list.count())
        self.assertEqual(2, linked_list.pop_back())
        self.assertEqual(1, linked_list.count())
        self.assertEqual(1, linked_list.pop_back())
        self.assertEqual(0, linked_list.count())
        self.assertEqual(True, linked_list.is_empty())

        l1 = SinglyLinkedList()
        l2 = SinglyLinkedList()

        self.assertEqual(True, l1 == l2)

        l1.push_back(1)
        self.assertEqual(False, l1 == l2)
        l2.push_back(1)
        self.assertEqual(True, l1 == l2)
        l1.push_back(2)
        self.assertEqual(False, l1 == l2)
        l2.push_back(2)
        self.assertEqual(True, l1 == l2)

        self.assertEqual(SinglyLinkedList([1, 2]), l2)

        ll = SinglyLinkedList([1, 2, 3])
        n = ll.head
        m = n.next
        q = ll.remove_node(n)
        self.assertEqual(SinglyLinkedList([2, 3]), ll)


if __name__ == '__main__':
    unittest.main()
