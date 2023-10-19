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

    def front(self):
        if self.head:
            return self.head.value
        else:
            return None

    def back(self):
        if not self.head:
            return None
        p = self.head
        while p.next:
            p = p.next
        return p.value

    def push_front(self, v):
        new_node = self.Node(v)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

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

    def pop_front(self):
        if not self.head:
            return None
        if self.head.next:
            v = self.head.value
            self.head = self.head.next
            return v
        else:
            v = self.head.value
            self.head = None
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

    def clear(self):
        while self.head:
            self.pop_front()


class Test(unittest.TestCase):
    def test_basic(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(True, linked_list.is_empty())
        self.assertEqual(None, linked_list.back())
        self.assertEqual(None, linked_list.front())
        self.assertEqual(0, linked_list.count())
        self.assertEqual([], linked_list.as_list())
        linked_list.push_back(1)
        self.assertEqual(1, linked_list.count())
        self.assertEqual([1], linked_list.as_list())
        self.assertEqual(False, linked_list.is_empty())
        self.assertEqual(1, linked_list.back())
        self.assertEqual(1, linked_list.front())
        linked_list.push_back(2)
        self.assertEqual([1, 2], linked_list.as_list())
        self.assertEqual(1, linked_list.front())
        self.assertEqual(2, linked_list.back())
        self.assertEqual(2, linked_list.count())
        self.assertEqual(2, linked_list.pop_back())
        self.assertEqual(1, linked_list.front())
        self.assertEqual(1, linked_list.back())
        self.assertEqual(1, linked_list.count())
        self.assertEqual(1, linked_list.pop_back())
        self.assertEqual(0, linked_list.count())
        self.assertEqual(None, linked_list.back())
        self.assertEqual(None, linked_list.front())
        self.assertEqual(True, linked_list.is_empty())

    def test_equality(self):
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

    def test_removal(self):
        ll = SinglyLinkedList([1, 2, 3])
        n = ll.head
        m = n.next
        q = ll.remove_node(n)
        self.assertEqual(SinglyLinkedList([2, 3]), ll)

    def test_push(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(True, linked_list.is_empty())
        self.assertEqual(0, linked_list.count())
        linked_list.push_front(1)
        self.assertEqual([1], linked_list.as_list())
        self.assertEqual(1, linked_list.count())
        linked_list.push_front(2)
        self.assertEqual(2, linked_list.count())
        self.assertEqual([2, 1], linked_list.as_list())
        linked_list.push_back(3)
        self.assertEqual([2, 1, 3], linked_list.as_list())

    def test_pop(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(None, linked_list.pop_front())
        self.assertEqual(None, linked_list.pop_back())
        linked_list.push_back(1)
        self.assertEqual([1], linked_list.as_list())
        self.assertEqual(1, linked_list.pop_front())
        linked_list.push_back(2)
        self.assertEqual(2, linked_list.pop_front())
        linked_list.push_back(3)
        linked_list.push_back(4)
        self.assertEqual([3, 4], linked_list.as_list())
        self.assertEqual(4, linked_list.pop_back())
        self.assertEqual(3, linked_list.pop_back())
        linked_list.push_back(5)
        linked_list.push_back(6)
        self.assertEqual(5, linked_list.pop_front())
        self.assertEqual(6, linked_list.pop_front())
        self.assertEqual(None, linked_list.pop_front())

    def test_clear(self):
        linked_list = SinglyLinkedList()
        linked_list.clear()
        self.assertEqual(True, linked_list.is_empty())
        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertEqual([1, 2, 3], linked_list.as_list())
        linked_list.clear()
        self.assertEqual(True, linked_list.is_empty())


if __name__ == '__main__':
    unittest.main()
