import timeit

from timeit import Timer

access_zero = Timer("nums[0]", "from __main__ import nums")
access_last = Timer("nums[9999999]", "from __main__ import nums")

nums = list(range(10000000))
print(f"{access_zero.timeit(number=10000):.10f}")

nums = list(range(10000000))
print(f"{access_last.timeit(number=10000):.10f}")
