import unittest
from random import shuffle


def merge_sort(nums: list) -> list:
    pass


class TestMergeSort(unittest.TestCase):
    def test_312(self):
        self.assertEqual(merge_sort([3, 1, 2]), [1, 2, 3])

    def test_21(self):
        self.assertEqual(merge_sort([2, 1]), [1, 2])

    def test_1(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_large(self):
        sorted_list = list(range(1000))
        random_list = sorted_list.copy()
        shuffle(random_list)
        self.assertEqual(merge_sort(random_list), sorted_list)


if __name__ == "__main__":
    unittest.main()
