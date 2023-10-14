import unittest

# Assume you have a method isSubstring. Decide whether a string s is a rotation of another string t
# using one single call to isSubstring. waterbottle is a rotation of erbottlewat


def is_rotation(s1, s2):
    s = s1 + s1
    if s.find(s2) != -1:
        return True
    else:
        return False


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(True, is_rotation("waterbottle", "erbottlewat"))
        self.assertEqual(False, is_rotation("hello", "heyyou"))


if __name__ == '__main__':
    unittest.main()
