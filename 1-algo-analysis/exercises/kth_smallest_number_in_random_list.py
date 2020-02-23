"""
4. Given a list of numbers in random order write a linear time algorithm to find the kth
smallest number in the list. Explain why your algorithm is linear.
5. Can you improve the algorithm from the previous problem to be O(n log(n))?
"""

import unittest
import random


def k_smallest_number(nums, target_smallest):
    if len(nums) == 1:
        return nums[0]


def k_smallest_number_log_linear(nums, target_smallest):
    pass


class TestKSmallestNumber(unittest.TestCase):

    def test_negitive_3(self):
        input = k_smallest_number([3, -1, -5, -8, 14, 9], 3)
        self.assertEqual(input, -1)

    def test_5_1(self):
        input = k_smallest_number([5], 1)
        self.assertEqual(input, 5)

    def test_21_2(self):
        input = k_smallest_number([2, 1], 2)
        self.assertEqual(input, 2)

    def test_489621_3(self):
        input = k_smallest_number([4, 8, 9, 6, 2, 1], 3)
        self.assertEqual(input, 4)

    def test_long_100(self):
        nums = list(range(1, 1000))
        random.shuffle(nums)
        input = k_smallest_number(nums, 100)
        self.assertEqual(input, 100)


if __name__ == "__main__":
    unittest.main()
