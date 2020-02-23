from models.stack import Stack
import unittest


def base_converter(number, base):
    num_stack = Stack()
    values = "0123456789ABCDEFGHIJKLMOPQ"

    while number > 0:
        num_stack.add(number % base)
        number = number // base

    converted_number = ""
    while not num_stack.is_empty():
        converted_number += values[num_stack.pop()]

    return converted_number


class TestBaseConverter(unittest.TestCase):
    def test_6_2(self):
        self.assertEqual(base_converter(6, 2), "110")

    def test_13399_2(self):
        self.assertEqual(base_converter(13399, 2), "11010001010111")

    def test_13399_8(self):
        self.assertEqual(base_converter(13399, 8), "32127")

    def test_13399_16(self):
        self.assertEqual(base_converter(13399, 16), "3457")

    def test_192_16(self):
        self.assertEqual(base_converter(192, 16), "C0")


if __name__ == "__main__":
    print(base_converter(25, 8))
    print(base_converter(256, 16))
    print(base_converter(26, 26))
    unittest.main()
