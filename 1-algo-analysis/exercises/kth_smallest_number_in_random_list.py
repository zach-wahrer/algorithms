"""
4. Given a list of numbers in random order write a linear time algorithm to find the kth
smallest number in the list. Explain why your algorithm is linear.
5. Can you improve the algorithm from the previous problem to be O(n log(n))?
"""

import unittest
import random


# O(n) sort of?
def k_smallest_number_linear(nums, target_smallest):
    if not nums:
        return None

    target_queue = []

    for num in nums:

        if len(target_queue) < target_smallest:
            target_queue.append(num)
            target_queue.sort()

        elif num < target_queue[-1]:
            target_queue[-1] = num
            target_queue.sort()

    return target_queue[-1]


# O(n log(n))
def k_smallest_number(nums, target_smallest):
    if not nums:
        return None

    nums.sort()

    return nums[target_smallest - 1]


class TestKSmallestNumber(unittest.TestCase):

    def test_zero(self):
        input = k_smallest_number([1, 2, 3, 4, 5, 0, -1], 2)
        self.assertEqual(input, 0)

    def test_blank(self):
        input = k_smallest_number([], 1)
        self.assertEqual(input, None)

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
