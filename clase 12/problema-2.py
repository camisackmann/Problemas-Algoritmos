from collections import defaultdict

def max_palindrome_beauty(k, n, presents):
<<<<<<< HEAD
    regalos = {}
    for i in presents:
        if i[0] not in regalos:
            regalos[i[0]] = i[1]
        
        if regalos[i[0]] < i[1]:
            regalos[i[0]] = i[1]
    # print(regalos)
    max_palindromo = 0
    for key in regalos:
        if regalos[key] > 0:
            if key == key[::-1]:
                max_palindromo += regalos[key]
            elif key[::-1] in regalos:
                max_palindromo += ((regalos[key] + regalos[key[::-1]])/2)
    
    return max_palindromo

=======
    
>>>>>>> 4db42ed13c292a6c19dc80c0ce8bf55591f3eb93


# --- Test unitarios ---
import unittest

class TestMaxPalindromeBeauty(unittest.TestCase):

    def test_case_1(self):
        presents = [("abc", 3), ("cba", 4), ("aba", 2), ("def", -5)]
        self.assertEqual(max_palindrome_beauty(4, 3, presents), 9)  # 7 + 2 = 9

    def test_case_2(self):
        presents = [("abc", -3), ("cba", -2), ("aba", 1)]
        self.assertEqual(max_palindrome_beauty(3, 3, presents), 1)  # Solo el palíndromo "aba"

    def test_case_3(self):
        presents = [("abc", 2), ("cba", 3), ("abd", -2), ("def", -1)]
        self.assertEqual(max_palindrome_beauty(4, 3, presents), 5)  # 2 + 3 = 5

    def test_case_4(self):
        presents = [("madam", 3), ("madam", 5), ("hello", -10)]
        self.assertEqual(max_palindrome_beauty(3, 5, presents), 8)  # "madam" tiene belleza 5

    def test_case_5(self):
        presents = [("a", 10), ("a", -3)]
        self.assertEqual(max_palindrome_beauty(2, 1, presents), 10)  # La cadena "a" con belleza 10

if __name__ == '__main__':
    unittest.main()
