import unittest
from ctypes import c_int32
from bitstring import BitArray


def get_bit(v, i):
    return 1 if ((v & 1 << i) != 0) else 0


def set_bit(v, i):
    return v | (1 << i)


def clear_bit(v, i):
    return v & (~(1 << i))


def set_bit_to(v, i, bit_value):
    mask = ~(1 << i)
    bv = 1 if bit_value else 0
    return (v & mask) | (bv << i)


def b2i(s):
    """Convert a string to binary as integer"""
    return BitArray(bin=s).int


def insert_p_into_q(p, q, i, j):
    """
    Insertion: Given two 32-bits numbers, P and Q, and given j and i, insert M into N at position i through j
    You can assume that Q fits in the given range
    """
    qq = q << i
    mask_right = ~0 << (j + 1)
    mask_left = (1 << i) - 1
    mask = mask_left | mask_right
    pp = p & mask
    return pp | qq


def double_to_binary(value):
    """
    Double to binary: convert a floating point number between 0 and 1 to a 32-bits binary.
    If the number cannot be correctly represent, return "ERROR"
    """
    s = ""
    v = value
    f = 0.5
    while v > 0:
        if len(s) > 32:
            return "ERROR"

        if v >= f:
            s += "1"
            v -= f
        else:
            s += "0"
        f /= 2
    return "0." + s


def flip_to_win(value):
    """
    Flip bit to win: Given an integer K. Write code to find the length of the
    longest sequences of 1 you can find by flipping a bit from 0 to 1.
    """
    longest_so_far = 1
    current_length = 0
    previous_length = 0
    while value != 0:
        if value & 1 == 1:
            current_length += 1
        elif value & 1 == 0:
            previous_length = 0 if value & 2 == 0 else current_length
            current_length = 0
        longest_so_far = max(previous_length + current_length + 1, longest_so_far)
        value = int(value / 2)
    return longest_so_far


class Test(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(1, get_bit(8, 3))
        self.assertEqual(0, get_bit(8, 2))
        self.assertEqual(0, get_bit(8, 1))
        self.assertEqual(0, get_bit(8, 0))
        self.assertEqual(1, get_bit(9, 0))

        self.assertEqual(9, set_bit(8, 0))
        self.assertEqual(10, set_bit(8, 1))

        self.assertEqual(0, clear_bit(8, 3))
        self.assertEqual(8, clear_bit(8, 2))
        self.assertEqual(8, clear_bit(9, 0))

        self.assertEqual(8, set_bit_to(8, 0, 0))
        self.assertEqual(9, set_bit_to(8, 0, 1))
        self.assertEqual(24, set_bit_to(8, 4, 1))

    def test_insert(self):
        self.assertEqual("0b1001", bin(insert_p_into_q(8, 1, 0, 0)))
        self.assertEqual("0b10011100", bin(insert_p_into_q(128, 7, 2, 4)))
        self.assertEqual("0b10111000", bin(insert_p_into_q(128, 7, 3, 5)))

    def test_double_to_binary(self):
        self.assertEqual("0.101", double_to_binary(0.625))
        self.assertEqual("ERROR", double_to_binary(1 / 3))
        self.assertEqual("0.01", double_to_binary(1 / 4))

    def test_flip(self):
        self.assertEqual(2, flip_to_win(8))
        self.assertEqual(4, flip_to_win(7))
        self.assertEqual(3, flip_to_win(10))


if __name__ == '__main__':
    unittest.main()
