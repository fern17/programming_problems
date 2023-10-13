import unittest

# Implement an algorithm to determine if a string has all unique characters. What if you cannot
# use additional data structures


def is_unique_with_set(input_string):
    charset = set()
    for c in input_string:
        charset.add(c)
    return len(charset) == len(input_string)


def test_is_unique_with_bitvector(input_string):
    bitvector = [False] * 128
    for i in range(0, len(input_string)):
        v = ord(input_string[i])
        if bitvector[v]:
            return False
        bitvector[v] = True
    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_unique_with_set("abc"), True)
        self.assertEqual(is_unique_with_set("abca"), False)
        self.assertEqual(is_unique_with_set(""), True)
        self.assertEqual(is_unique_with_set("aaaaa"), False)

        self.assertEqual(test_is_unique_with_bitvector("abc"), True)
        self.assertEqual(test_is_unique_with_bitvector("abca"), False)
        self.assertEqual(test_is_unique_with_bitvector(""), True)
        self.assertEqual(test_is_unique_with_bitvector("aaaaa"), False)


if __name__ == '__main__':
    unittest.main()
