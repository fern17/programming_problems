import unittest

# Given a string s, return a new string cs where successive n repeated characters c are reduced to nc
# aaaabbbccd => 4a3b2c1d
# If the compression would give a longer string, return the initial string


def compress_string(s):
    compressed = []
    compression_rate = 1

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            compressed.append(str(compression_rate) + s[i-1])
            compression_rate = 0
        compression_rate += 1
    compressed.append(str(compression_rate) + s[-1])
    cs = ''.join(compressed)
    if len(cs) >= len(s):
        return s
    else:
        return cs



class Test(unittest.TestCase):
    def test(self):
        self.assertEqual("a", compress_string("a"))
        self.assertEqual("aa", compress_string("aa"))
        self.assertEqual("3a", compress_string("aaa"))
        self.assertEqual("3a3b3c", compress_string("aaabbbccc"))
        self.assertEqual("4a3b2c1d", compress_string("aaaabbbccd"))
        self.assertEqual("4b3a3b3c", compress_string("bbbbaaabbbccc"))


if __name__ == '__main__':
    unittest.main()
