import timeit

from timeit import Timer

get_item1 = Timer("nums[0]", "from __main__ import nums")
get_item2 = Timer("nums[9999999]", "from __main__ import nums")

set_item1 = Timer("nums[1000000000] = 1", "from __main__ import nums")
set_item2 = Timer("nums[0] = 1", "from __main__ import nums")

nums = {i: None for i in range(10000000)}
print(f"{get_item1.timeit(number=10000):.10f}")

nums = {i: None for i in range(10000000)}
print(f"{get_item2.timeit(number=10000):.10f}")

nums = {i: None for i in range(10000000)}
print(f"{set_item1.timeit(number=10000):.10f}")

nums = {i: None for i in range(10000000)}
print(f"{set_item2.timeit(number=10000):.10f}")
