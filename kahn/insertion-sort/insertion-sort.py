import unittest
from random import shuffle


def insertion_sort(numbers: list) -> list:

    for index in range(1, len(numbers)):
        value_to_insert = numbers[index]
        while index > 0 and value_to_insert < numbers[index - 1]:
            numbers[index] = numbers[index - 1]
            index -= 1
        numbers[index] = value_to_insert

    return numbers


class TestInsertionSort(unittest.TestCase):
    def test_large(self):
        original_list = list(range(1000))
        shuffle_list = original_list.copy()
        shuffle(shuffle_list)
        self.assertEqual(insertion_sort(shuffle_list), original_list)


if __name__ == "__main__":
    unittest.main()
