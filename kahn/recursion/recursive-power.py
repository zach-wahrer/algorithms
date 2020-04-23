import unittest


def get_power(base, exponent) -> int:
    if exponent == 0:
        return 1

    if exponent > 0 and exponent % 2 == 0:
        result = get_power(base, exponent / 2)
        return result * result
    elif exponent > 0:
        return get_power(base, exponent - 1) * base
    else:
        return 1 / get_power(base, -exponent)


class TestPower(unittest.TestCase):
    def test_3_0(self):
        self.assertEqual(get_power(3, 0), 1)

    def test_3_1(self):
        self.assertEqual(get_power(3, 1), 3)

    def test_3_2(self):
        self.assertEqual(get_power(3, 2), 9)

    def test_3_minus1(self):
        self.assertEqual(get_power(3, -1), 1 / 3)


if __name__ == "__main__":
    unittest.main()
