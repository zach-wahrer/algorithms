def fib_recursive(seq_num):

    memoize = {0: 0, 1: 1}

    def _fib_recursive(seq_num):
        if seq_num not in memoize:
            memoize[seq_num] = _fib_recursive(seq_num - 1) + _fib_recursive(seq_num - 2)
        return memoize[seq_num]

    return _fib_recursive(seq_num)


def fib_loop(seq_num):
    start = 0
    next = 1

    for _ in range(seq_num - 1):
        tmp = next
        next = start + next
        start = tmp
    return(next)


print(fib_loop(100))

print(fib_recursive(100))
