import sys
sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest

# Implement a StackOfStacks class that contains a set of stacks of a maximum threshold size.
# No stack size could be greater than this given threshold
# The stack should behave like a normal Stack for the client


class StackOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []
        self.stacks.append(SLL.SinglyLinkedList())
        self.current_stack = 0
        self.stacks_sizes = []
        self.stacks_sizes.append(0)

    def push(self, value):
        if self.stacks_sizes[self.current_stack] >= self.threshold:
            self.stacks.append(SLL.SinglyLinkedList())
            self.current_stack += 1
            self.stacks_sizes.append(0)
        self.stacks[self.current_stack].push_front(value)
        self.stacks_sizes[self.current_stack] += 1

    def pop(self):
        if self.current_stack == -1:
            return None
        if self.stacks_sizes[self.current_stack] == 1:
            v = self.stacks[self.current_stack].pop_front()
            self.stacks_sizes.pop()
            self.stacks.pop()
            self.current_stack -= 1
            return v
        else:
            if self.stacks_sizes[self.current_stack] == 0:
                return None
            else:
                self.stacks_sizes[self.current_stack] -= 1
                return self.stacks[self.current_stack].pop_front()

    def as_list(self):
        list_of_stacks = []
        for s in self.stacks:
            list_of_stacks = s.as_list() + list_of_stacks
        return list_of_stacks


class Test(unittest.TestCase):
    def test(self):
        ss = StackOfStacks(3)
        self.assertEqual([], ss.as_list())
        self.assertEqual(None, ss.pop())
        ss.push(1)
        ss.push(2)
        ss.push(3)
        self.assertEqual([3, 2, 1], ss.as_list())
        ss.push(4)
        self.assertEqual([4, 3, 2, 1], ss.as_list())
        ss.push(5)
        self.assertEqual([5, 4, 3, 2, 1], ss.as_list())
        self.assertEqual(5, ss.pop())
        self.assertEqual([4, 3, 2, 1], ss.as_list())
        self.assertEqual(4, ss.pop())
        self.assertEqual([3, 2, 1], ss.as_list())
        self.assertEqual(3, ss.pop())
        self.assertEqual([2, 1], ss.as_list())
        self.assertEqual(2, ss.pop())
        self.assertEqual([1], ss.as_list())
        self.assertEqual(1, ss.pop())
        self.assertEqual(None, ss.pop())



if __name__ == '__main__':
    unittest.main()
