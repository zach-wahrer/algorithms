import unittest
from random import shuffle


def selection_sort(numbers: list) -> list:
    p1 = 0
    p2 = 1

    while p1 < len(numbers):
        lowest_seen = numbers[p1]
        lowest_index = p1

        while p2 < len(numbers):
            if numbers[p2] < lowest_seen:
                lowest_seen = numbers[p2]
                lowest_index = p2
            p2 += 1

        numbers[p1], numbers[lowest_index] = numbers[lowest_index], numbers[p1]
        p1 += 1
        p2 = p1 + 1

    return numbers


class TestSelectionSort(unittest.TestCase):
    def test_large(self):
        original_numbers = [i for i in range(1000)]
        shuffled_numbers = original_numbers.copy()
        shuffle(shuffled_numbers)
        self.assertEqual(selection_sort(shuffled_numbers), original_numbers)


if __name__ == "__main__":
    unittest.main()
