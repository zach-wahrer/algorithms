import unittest
from self_check2 import generate_string, score_string

goal_string = "this is only a test"


class TestStrings(unittest.TestCase):

    def test_generate(self):
        input = generate_string(len(goal_string))
        self.assertEqual(len(input), len(goal_string))

    def test_score_100(self):
        input = score_string(goal_string, goal_string)
        self.assertEqual(input, 100)

    def test_score_0(self):
        input = score_string(("0" * len(goal_string)), goal_string)
        self.assertEqual(input, 0)

    def test_score_52(self):
        input = score_string("this is            ", goal_string)
        self.assertEqual(input, 52.631578947368425)


if __name__ == "__main__":
    unittest.main()
