"""
Self Check
Write two Python functions to find the minimum number in a list. The first function should
compare each number to every other number on the list. O(n**2). The second function should be
linear O(n).
"""

import unittest
import random
from time import time

numbers = [i for i in range(random.randint(100, 1000), random.randint(1001, 100000))]
random.shuffle(numbers)


def find_min_in_list_quadradic(numbers):
    start = time()
    lowest_found = numbers[0]
    for initial_number in numbers:
        for checking_number in numbers:
            if initial_number < checking_number and initial_number < lowest_found:
                lowest_found = initial_number
    finish = time()
    print("quadratic took: ", finish - start)
    return lowest_found


def find_min_in_list_linear(numbers):
    start = time()
    lowest_found = numbers[0]
    for number in numbers:
        if number < lowest_found:
            lowest_found = number
    finish = time()
    print("linear1 took: ", finish - start)
    return lowest_found


def find_min_in_list_linear2(numbers):
    start = time()
    minimum = min(numbers)
    finish = time()
    print("linear2 took: ", finish - start)
    return(minimum)


print(find_min_in_list_quadradic(numbers))
print(find_min_in_list_linear(numbers))
print(find_min_in_list_linear2(numbers))
