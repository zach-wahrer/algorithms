
import random


def shell_sort(sort_list):
    sublist_count = len(sort_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(sort_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    return sort_list


def gap_insertion_sort(sort_list, start, gap):
    for i in range(start + gap, len(sort_list), gap):
        current_value = sort_list[i]
        position = i
        while position >= gap and sort_list[position - gap] > current_value:
            sort_list[position] = sort_list[position - gap]
            position = position - gap

        sort_list[position] = current_value


sort_me = list(range(1000))
random.shuffle(sort_me)

print(shell_sort(sort_me))
