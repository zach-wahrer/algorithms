def list_sum(num_list):

    def _recursive_sum(numbers):
        if len(numbers) == 1:
            return numbers[0]
        return numbers[0] + _recursive_sum(numbers[1:])

    return _recursive_sum(num_list)


print(list_sum([1, 2, 3, 4, 5]))
print(list_sum([1, 2]))
print(list_sum([1]))
print(list_sum(list(range(997))))
