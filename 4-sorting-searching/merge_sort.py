import random


def merge_sort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        left_half = sort_list[:mid]
        right_half = sort_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        sort_list_pointer = 0
        left_pointer = 0
        right_pointer = 0

        while left_pointer < len(left_half) and right_pointer < len(right_half):
            if left_half[left_pointer] < right_half[right_pointer]:
                sort_list[sort_list_pointer] = left_half[left_pointer]
                left_pointer += 1
            else:
                sort_list[sort_list_pointer] = right_half[right_pointer]
                right_pointer += 1
            sort_list_pointer += 1

        while left_pointer < len(left_half):
            sort_list[sort_list_pointer] = left_half[left_pointer]
            left_pointer += 1
            sort_list_pointer += 1

        while right_pointer < len(right_half):
            sort_list[sort_list_pointer] = right_half[right_pointer]
            right_pointer += 1
            sort_list_pointer += 1


sort_me = list(range(1000))
random.shuffle(sort_me)
merge_sort(sort_me)
print(sort_me)
