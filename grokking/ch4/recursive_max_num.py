def max_num_with_tracking_var(collection):

    def _recursive_max(items, max_seen=float('-inf')):
        if len(items) < 2:
            return items[0] if items[0] > max_seen else max_seen

        max_seen = items[0] if items[0] > max_seen else max_seen

        return _recursive_max(items[1:], max_seen)

    return _recursive_max(collection)


def max_num(collection):

    def _recursive_max(items):
        if len(items) == 2:
            return items[0] if items[0] > items[1] else items[1]

        sub_max = _recursive_max(items[1:])

        return items[0] if items[0] > sub_max else sub_max

    return _recursive_max(collection)


print(max_num([1, 2, 3, 4, 5]))
print(max_num([100, 2, 3, 4, 5]))
print(max_num([100, 2, 5000, 4, 5]))
