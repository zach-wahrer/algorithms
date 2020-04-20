import random


def insertion_sort(sort_list):
    for index in range(1, len(sort_list)):

        current_value = sort_list[index]

        while index > 0 and current_value < sort_list[index - 1]:
            sort_list[index] = sort_list[index - 1]
            index -= 1
        sort_list[index] = current_value

    return sort_list


sort_me = list(range(1000))
random.shuffle(sort_me)

print(insertion_sort(sort_me))
