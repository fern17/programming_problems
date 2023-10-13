import unittest

# Problem description


def something():
    return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(True, something())


if __name__ == '__main__':
    unittest.main()
