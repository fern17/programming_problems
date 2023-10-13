import unittest

# Given a string, write a function to check if it is a permutation of a palindrome.


def is_palindrome_permutation(s):
    s = s.lower()
    char_count = [False] * 128
    for i in range(len(s)):
        if s[i].isalpha():
            c = ord(s[i])
            char_count[c] = not char_count[c]
    return char_count.count(True) <= 1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(True, is_palindrome_permutation("a"))
        self.assertEqual(False, is_palindrome_permutation("ab"))
        self.assertEqual(True, is_palindrome_permutation("aba"))
        self.assertEqual(False, is_palindrome_permutation("abcas3xa"))
        self.assertEqual(True, is_palindrome_permutation("aaabbaaa"))
        self.assertEqual(True, is_palindrome_permutation("Tact Coa"))


if __name__ == '__main__':
    unittest.main()
