import sys

sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest


# Implement a queue with two stacks


class QueueWithStacks:
    def __init__(self):
        self.stack = SLL.SinglyLinkedList()
        self.buffer_stack = SLL.SinglyLinkedList()

    def push(self, value):
        self.stack.push_front(value)

    def pop(self):
        self.buffer_stack.clear()
        v = None
        while self.stack.head:
            self.buffer_stack.push_front(self.stack.pop_front())

        v = self.buffer_stack.pop_front()

        while self.buffer_stack.head:
            self.stack.push_front(self.buffer_stack.pop_front())

        return v

    def as_list(self):
        return self.stack.as_list()


class Test(unittest.TestCase):
    def test(self):
        ss = QueueWithStacks()
        self.assertEqual(None, ss.pop())
        ss.push(1)
        ss.push(2)
        ss.push(3)
        ss.push(4)
        ss.push(5)
        self.assertEqual([5, 4, 3, 2, 1], ss.as_list())
        self.assertEqual(1, ss.pop())
        self.assertEqual([5, 4, 3, 2], ss.as_list())
        self.assertEqual(2, ss.pop())
        self.assertEqual([5, 4, 3], ss.as_list())
        self.assertEqual(3, ss.pop())
        self.assertEqual([5, 4], ss.as_list())
        self.assertEqual(4, ss.pop())
        self.assertEqual([5], ss.as_list())
        self.assertEqual(5, ss.pop())
        self.assertEqual(None, ss.pop())


if __name__ == '__main__':
    unittest.main()
