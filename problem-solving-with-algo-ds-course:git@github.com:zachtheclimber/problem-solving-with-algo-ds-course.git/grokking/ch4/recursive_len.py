def length(collection):
    def _recursive_len(items):
        if len(items) == 1:
            return 1
        return 1 + _recursive_len(items[1:])

    return _recursive_len(collection)


print(length([1, 2, 3, 4, 5, 6]))
print(length([1, 2, 3, 4, 5, 6, 'a', 'b', 'c']))
print(length([1]))
