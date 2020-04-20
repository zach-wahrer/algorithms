import random


def bubble_sort(sort_list):
    for iteration in range(len(sort_list) - 1, 0, -1):
        for num in range(iteration):
            if sort_list[num] > sort_list[num + 1]:
                sort_list[num], sort_list[num + 1] = sort_list[num + 1], sort_list[num]
    return sort_list


sort_me = list(range(1000))
random.shuffle(sort_me)

print(bubble_sort(sort_me))
