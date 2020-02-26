import random


def selection_sort(sort_list):
    for iteration in range(len(sort_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(iteration + 1):
            if sort_list[location] > sort_list[pos_of_max]:
                pos_of_max = location
        sort_list[pos_of_max], sort_list[iteration] = sort_list[iteration], sort_list[pos_of_max]
        pos_of_max = 0
    return sort_list


sort_me = list(range(1000))
random.shuffle(sort_me)

print(selection_sort(sort_me))
