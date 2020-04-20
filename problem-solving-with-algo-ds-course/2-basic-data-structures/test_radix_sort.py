from radix_sort import radix_sorting
import unittest
import random


class TestRadixSort(unittest.TestCase):
    def test_large(self):
        nums_sorted = list(range(1000000))
        nums_random = nums_sorted.copy()
        random.shuffle(nums_random)
        self.assertEqual(radix_sorting(nums_random), nums_sorted)


if __name__ == "__main__":
    unittest.main()
