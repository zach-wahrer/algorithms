import unittest


def get_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


class TestFactorial(unittest.TestCase):
    def test_5(self):
        self.assertEqual(get_factorial(5), 120)

    def test_0(self):
        self.assertEqual(get_factorial(0), 1)


if __name__ == "__main__":
    unittest.main()
