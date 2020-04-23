import unittest
from random import shuffle


def merge_sort(nums: list) -> list:

    if len(nums) < 2:
        return nums

    mid = len(nums) // 2

    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]), nums)


def merge(first_half: list, second_half: list, results: list) -> list:
    ptr1 = ptr2 = results_ptr = 0
    while ptr1 < len(first_half) and ptr2 < len(second_half):
        if first_half[ptr1] < second_half[ptr2]:
            results[results_ptr] = first_half[ptr1]
            ptr1 += 1
        else:
            results[results_ptr] = second_half[ptr2]
            ptr2 += 1
        results_ptr += 1

    while ptr1 < len(first_half):
        results[results_ptr] = first_half[ptr1]
        ptr1 += 1
        results_ptr += 1

    while ptr2 < len(second_half):
        results[results_ptr] = second_half[ptr2]
        ptr2 += 1
        results_ptr += 1

    return results


class TestMergeSort(unittest.TestCase):
    def test_312(self):
        self.assertEqual(merge_sort([3, 1, 2]), [1, 2, 3])

    def test_21(self):
        self.assertEqual(merge_sort([2, 1]), [1, 2])

    def test_1(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_large(self):
        sorted_list = list(range(2000))
        random_list = sorted_list.copy()
        shuffle(random_list)
        self.assertEqual(merge_sort(random_list), sorted_list)


if __name__ == "__main__":
    unittest.main()
