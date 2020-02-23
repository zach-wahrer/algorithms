from models.stack import Stack
import unittest


def infix_to_postfix(expression):
    pass


class TestInfixToPostfix(unittest.TestCase):
    def test_1(self):
        self.assertEqual(infix_to_postfix("( A + B ) * ( C + D )"), "A B + C D + *")

    def test_2(self):
        self.assertEqual(infix_to_postfix("( A + B ) * C"), "A B + C *")

    def test_3(self):
        self.assertEqual(infix_to_postfix("A + B * C"), "A B C * +")


if __name__ == "__main__":
    unittest.main()
