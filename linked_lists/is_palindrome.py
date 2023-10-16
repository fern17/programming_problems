import sys
sys.path.insert(0, "../data_structures")
import SinglyLinkedList as SLL

import unittest

# Write a  function to check if a linked list is a palindrome

def is_palindrome_v1(forward_list):
    reversed_list = SLL.SinglyLinkedList()
    p = forward_list.head
    while p:
        if p.value is not None:
            reversed_list.push_front(p.value)
            p = p.next
    return reversed_list == forward_list


def is_palindrome_v2(l):
    li = SLL.SinglyLinkedList()
    p = l.head
    c = 0
    while p:
        c += 1
        li.push_front(p.value)
        p = p.next

    p = l.head
    q = li.head
    i = 0
    half = int(c / 2)
    while p and q and i < half:
        if p.value != q.value:
            return False
        p = p.next
        q = q.next
        c += 1
    return True

class Test(unittest.TestCase):
    def test_v1(self):
        self.assertEqual(True, is_palindrome_v1(SLL.SinglyLinkedList([])))
        self.assertEqual(True, is_palindrome_v1(SLL.SinglyLinkedList([1])))
        self.assertEqual(False, is_palindrome_v1(SLL.SinglyLinkedList([1, 2])))
        self.assertEqual(True, is_palindrome_v1(SLL.SinglyLinkedList([1, 2, 1])))
        self.assertEqual(False, is_palindrome_v1(SLL.SinglyLinkedList([1, 2, 1, 3])))
        self.assertEqual(True, is_palindrome_v1(SLL.SinglyLinkedList([1, 2, 3, 2, 1])))
        self.assertEqual(False, is_palindrome_v1(SLL.SinglyLinkedList([1, 2, 3, 2])))
        self.assertEqual(True, is_palindrome_v1(SLL.SinglyLinkedList([1, 1, 1])))
        self.assertEqual(True, is_palindrome_v1(SLL.SinglyLinkedList([1, 1, 1, 1])))

    def test_v2(self):
        self.assertEqual(True,  is_palindrome_v2(SLL.SinglyLinkedList([])))
        self.assertEqual(True,  is_palindrome_v2(SLL.SinglyLinkedList([1])))
        self.assertEqual(False, is_palindrome_v2(SLL.SinglyLinkedList([1, 2])))
        self.assertEqual(True,  is_palindrome_v2(SLL.SinglyLinkedList([1, 2, 1])))
        self.assertEqual(False, is_palindrome_v2(SLL.SinglyLinkedList([1, 2, 1, 3])))
        self.assertEqual(True,  is_palindrome_v2(SLL.SinglyLinkedList([1, 2, 3, 2, 1])))
        self.assertEqual(False, is_palindrome_v2(SLL.SinglyLinkedList([1, 2, 3, 2])))
        self.assertEqual(True,  is_palindrome_v2(SLL.SinglyLinkedList([1, 1, 1])))
        self.assertEqual(True,  is_palindrome_v2(SLL.SinglyLinkedList([1, 1, 1, 1])))


if __name__ == '__main__':
    unittest.main()
