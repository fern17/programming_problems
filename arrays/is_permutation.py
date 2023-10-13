import unittest

# Given two strings, write a method to decide if one is a permutation of the other


def is_permutation_with_sort(str1, str2):
    if len(str1) != len(str2):
        return False

    s1 = sorted(str1)
    s2 = sorted(str2)

    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def is_permutation_counting(str1, str2):
    if len(str1) != len(str2):
        return False
    char_count_s1 = [0] * 128
    char_count_s2 = [0] * 128
    for i in range(0, len(str1)):
        char_count_s1[ord(str1[i])] += 1
        char_count_s2[ord(str2[i])] += 1

    for i in range(0, len(char_count_s1)):
        if char_count_s1[i] != char_count_s2[i]:
            return False
    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_permutation_with_sort("abc", "bca"), True)
        self.assertEqual(is_permutation_with_sort("abc", "dca"), False)
        self.assertEqual(is_permutation_with_sort("a", "a"), True)
        self.assertEqual(is_permutation_with_sort("a", "ab"), False)

        self.assertEqual(is_permutation_counting("abc", "bca"), True)
        self.assertEqual(is_permutation_counting("abc", "dca"), False)
        self.assertEqual(is_permutation_counting("a", "a"), True)
        self.assertEqual(is_permutation_counting("a", "ab"), False)


if __name__ == '__main__':
    unittest.main()
