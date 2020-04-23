import unittest


def get_factorial(num):
    return num * get_factorial(num - 1) if num > 0 else 1


class TestFactorial(unittest.TestCase):
    def test_5(self):
        self.assertEqual(get_factorial(5), 120)

    def test_0(self):
        self.assertEqual(get_factorial(0), 1)


if __name__ == "__main__":
    unittest.main()
