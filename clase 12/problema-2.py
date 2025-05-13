from collections import defaultdict

def max_palindrome_beauty(k, n, presents):


# --- Test unitarios ---
import unittest

class TestMaxPalindromeBeauty(unittest.TestCase):

    def test_case_1(self):
        presents = [("abc", 3), ("cba", 4), ("aba", 2), ("def", -5)]
        self.assertEqual(max_palindrome_beauty(4, 3, presents), 9)

    def test_case_2(self):
        presents = [("abc", -3), ("cba", -2), ("aba", 1)]
        self.assertEqual(max_palindrome_beauty(3, 3, presents), 1)

    def test_case_3(self):
        presents = [("abc", 2), ("cba", 3), ("abd", -2), ("def", -1)]
        self.assertEqual(max_palindrome_beauty(4, 3, presents), 5) 

    def test_case_4(self):
        presents = [("madam", 3), ("madam", 5), ("hello", -10)]
        self.assertEqual(max_palindrome_beauty(3, 5, presents), 8)

    def test_case_5(self):
        presents = [("a", 10), ("a", -3)]
        self.assertEqual(max_palindrome_beauty(2, 1, presents), 10)

if __name__ == '__main__':
    unittest.main()
