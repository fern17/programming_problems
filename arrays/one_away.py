import unittest

# Write a function to check if two strings are one or zero edits away. An edit could be adding removing
# or replacing a character


def one_edit_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    i = 0
    j = 0

    if len(str1) > len(str2):
        str1, str2 = str2, str1
    has_edit = False
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if not has_edit:
                has_edit = True
            else:
                return False
            if len(str1) == len(str2):
                i += 1
        else:
            i += 1
        j += 1
    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(True, one_edit_away("abc", "abc"))
        self.assertEqual(True, one_edit_away("abc", "abcd"))
        self.assertEqual(True, one_edit_away("abc", "dabc"))
        self.assertEqual(False, one_edit_away("abc", "adebc"))
        self.assertEqual(False, one_edit_away("adebc", "abc"))
        self.assertEqual(False, one_edit_away("abc", "def"))
        self.assertEqual(False, one_edit_away("abc", "cde"))
        self.assertEqual(False, one_edit_away("abc", "abcabc"))
        self.assertEqual(False, one_edit_away("pale", "bake"))
        self.assertEqual(True, one_edit_away("pale", "ple"))
        self.assertEqual(True, one_edit_away("pales", "pale"))
        self.assertEqual(True, one_edit_away("pale", "bale"))


if __name__ == '__main__':
    unittest.main()
