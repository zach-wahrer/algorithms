def quick_sort(to_sort: list) -> list:
    if len(to_sort) < 2:
        return to_sort

    lt = [i for i in to_sort[1:] if i < to_sort[0]]
    gt = [i for i in to_sort[1:] if i > to_sort[0]]
    return quick_sort(lt) + [to_sort[0]] + quick_sort(gt)


print(quick_sort([1, 10, 99, 8, 3, 2, 14]))
