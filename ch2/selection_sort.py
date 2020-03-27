import unittest
import random


def sel_sort(items: list, order="asc") -> None:

    def _find_next_max(items):
        max_in_list = {"index": float("-inf"), "value": float("-inf")}
        for index, value in enumerate(items):
            if value > max_in_list['value']:
                max_in_list['value'] = value
                max_in_list['index'] = index
        return max_in_list['index']

    def _find_next_min(items):
        min_in_list = {"index": float("+inf"), "value": float("+inf")}
        for index, value in enumerate(items):
            if value < min_in_list['value']:
                min_in_list['value'] = value
                min_in_list['index'] = index
        return min_in_list['index']

    if order == "asc":
        pointer = 0
        while pointer < len(items):
            min_index = _find_next_min(items[pointer:])
            items[pointer], items[min_index + pointer] = items[min_index + pointer], items[pointer]
            pointer += 1

        return items

    else:
        pointer = 0
        while pointer < len(items):
            max_index = _find_next_max(items[pointer:])
            items[pointer], items[max_index + pointer] = items[max_index + pointer], items[pointer]
            pointer += 1
        return items


class TestSelectionSort(unittest.TestCase):

    def test_54321_asc(self):
        self.assertEqual(sel_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_54321_desc(self):
        self.assertEqual(sel_sort([1, 2, 3, 4, 5], "desc"), [5, 4, 3, 2, 1])

    def test_random_large_asc(self):
        large_list = list(range(1, 10000))
        shuffled_list = large_list.copy()
        random.shuffle(shuffled_list)
        self.assertEqual(sel_sort(shuffled_list), large_list)

    def test_random_large_desc(self):
        large_list = list(range(1, 10000))[::-1]
        shuffled_list = large_list.copy()
        random.shuffle(shuffled_list)
        self.assertEqual(sel_sort(shuffled_list, "desc"), large_list)


if __name__ == "__main__":
    unittest.main()
