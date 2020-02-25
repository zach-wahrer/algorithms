def reverse_list(in_list):
    reversed_list = []
    if len(in_list) == 1:
        return [in_list[0]]
    else:
        return reverse_list(in_list[1:]) + [in_list[0]]


print(reverse_list([1, 2, 3, 4, 5, 6]))
