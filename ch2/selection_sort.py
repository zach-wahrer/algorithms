import unittest
import random


def sel_sort(items: list, order="asc") -> None:
    pass


class TestSelectionSort(unittest.TestCase):

    def test_54321_asc(self):
        self.assertEqual(sel_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_54321_desc(self):
        self.assertEqual(sel_sort([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_random_large_asc(self):
        large_list = list(range(1, 10000))
        shuffled_list = random.shuffle(large_list.copy())
        self.assertEqual(sel_sort(shuffled_list), large_list)

    def test_random_large_desc(self):
        large_list = list(range(1, 10000))[::-1]
        shuffled_list = random.shuffle(large_list.copy())
        self.assertEqual(sel_sort(shuffled_list), large_list)


if __name__ == "__main__":
    unittest.main()
