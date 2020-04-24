import unittest
from random import shuffle


def quick_sort(nums: list) -> list:
    pass


class TestQuickSort(unittest.TestCase):
    def test_1(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_two(self):
        self.assertEqual(quick_sort([2, 1]), [1, 2])

    def test_three(self):
        self.assertEqual(quick_sort([2, 1, 3]), [1, 2, 3])

    def test_small(self):
        nums = [2, 1, 3, 100, 7, 9, 16]
        self.assertEqual(quick_sort(nums), [1, 2, 3, 7, 9, 16, 100])

    def test_large(self):
        sorted_nums = list(range(100))
        shuffled_nums = sorted_nums.copy()
        shuffle(shuffled_nums)
        self.assertEqual(quick_sort(shuffled_nums), sorted_nums)


if __name__ == "__main__":
    unittest.main()
