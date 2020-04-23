import unittest


def get_factorial(num):
    pass


class TestFactorial(unittest.TestCase):
    def test_5(self):
        self.assertEqual(get_factorial(5), 120)

    def test_0(self):
        self.assertEqual(get_factorial(0), 1)
