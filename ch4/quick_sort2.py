import random


def quick_sort(to_sort: list) -> list:
    if len(to_sort) < 2:
        return to_sort

    pivot = to_sort[random.randrange(0, len(to_sort))]
    lt, gt = [], []

    for i in to_sort:
        if i < pivot:
            lt.append(i)
        elif i > pivot:
            gt.append(i)

    return quick_sort(lt) + [pivot] + quick_sort(gt)


print(quick_sort([4, 99, 5, 8, 444, 89, 00, 33, 1]))
large_list = list(range(0, 1000000))
random.shuffle(large_list)
print(quick_sort(large_list))
