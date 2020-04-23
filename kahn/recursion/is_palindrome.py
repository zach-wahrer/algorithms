import unittest


def is_palindrome(string) -> bool:
    pass


class TestPalindrome(unittest.TestCase):
    def test_radar(self):
        self.assertTrue(is_palindrome("radar"))

    def test_reader(self):
        self.assertFalse(is_palindrome("reader"))

    def test_test(self):
        self.assertFalse(is_palindrome("test"))

    def test_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_a(self):
        self.assertTrue(is_palindrome("a"))

    def test_ra_ar(self):
        self.assertTrue(is_palindrome("ra ar"))


if __name__ == "__main__":
    unittest.main()
