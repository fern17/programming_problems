import unittest

# Write a method to replace all the spaces of a string for "%20"


def urlify(text):
    num_spaces = text.count(' ')
    url_text = list(text.rjust(num_spaces * 2 + len(text)))
    j = 0
    for i in range(len(text)):
        if text[i].isspace():
            url_text[j + 0] = '%'
            url_text[j + 1] = '2'
            url_text[j + 2] = '0'
            j += 3
        else:
            url_text[j] = text[i]
            j += 1
    return "".join(url_text)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(urlify(" "), "%20")
        self.assertEqual(urlify("  "), "%20%20")
        self.assertEqual(urlify(" hello "), "%20hello%20")
        self.assertEqual(urlify("hey you "), "hey%20you%20")


if __name__ == '__main__':
    unittest.main()
