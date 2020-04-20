import random


def quick_sort(sort_list):
    quick_sort_helper(sort_list, 0, len(sort_list) - 1)


def quick_sort_helper(sort_list, first, last):

    if first < last:
        split_point = partition(sort_list, first, last)

        quick_sort_helper(sort_list, first, split_point - 1)
        quick_sort_helper(sort_list, split_point + 1, last)


def partition(sort_list, first, last):
    pivot_value = sort_list[first]

    left_mark = first + 1
    right_mark = last

    while True:
        while left_mark <= right_mark and sort_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while sort_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            break

        else:
            sort_list[left_mark], sort_list[right_mark] = sort_list[right_mark], sort_list[left_mark]

    sort_list[first], sort_list[right_mark] = sort_list[right_mark], sort_list[first]

    return right_mark


sort_me = list(range(1000))
random.shuffle(sort_me)

quick_sort(sort_me)

print(sort_me)
