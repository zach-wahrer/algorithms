from models.stack import Stack
import unittest


def infix_to_postfix(expression):
    operator_stack = Stack()
    output = []
    token_list = expression.split()
    precedence = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for token in token_list:
        try:
            int(token)
            number = True
        except ValueError:
            number = False
        if token in chars or number:
            output.append(token)
        elif token == "(":
            operator_stack.add(token)
        elif token == ")":
            stack_token = operator_stack.pop()
            while stack_token != "(":
                output.append(stack_token)
                stack_token = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) and \
                    (precedence[operator_stack.peek()] >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.add(token)

    while not operator_stack.is_empty():
        output.append(operator_stack.pop())

    return " ".join(output)


class TestInfixToPostfix(unittest.TestCase):
    def test_1(self):
        self.assertEqual(infix_to_postfix("( A + B ) * ( C + D )"), "A B + C D + *")

    def test_2(self):
        self.assertEqual(infix_to_postfix("( A + B ) * C"), "A B + C *")

    def test_3(self):
        self.assertEqual(infix_to_postfix("A + B * C"), "A B C * +")

    def test_4(self):
        self.assertEqual(infix_to_postfix("A + B * C + D"), "A B C * + D +")

    def test_5(self):
        self.assertEqual(infix_to_postfix("A * B + C * D"), "A B * C D * +")

    def test_6(self):
        self.assertEqual(infix_to_postfix("A + B + C + D"), "A B + C + D +")


if __name__ == "__main__":
    print(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"))
    print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))
    unittest.main()
