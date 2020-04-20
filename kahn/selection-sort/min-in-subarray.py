from random import shuffle


def index_of_min(numbers: list) -> int:
    minimum = float("inf")
    location = -1

    for index, number in enumerate(numbers):
        if number < minimum:
            minimum = number
            location = index

    return location


numbers = [i for i in range(1000)]
shuffle(numbers)
print(index_of_min(numbers))
