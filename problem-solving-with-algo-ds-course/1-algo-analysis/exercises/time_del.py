import timeit

from timeit import Timer

del_list1 = Timer("del nums_list[0]", "from __main__ import nums_list")
del_list2 = Timer("del nums_list[998999]", "from __main__ import nums_list")

del_dict1 = Timer("del nums_dict[0]", "from __main__ import nums_dict")
del_dict2 = Timer("del nums_dict[99999]", "from __main__ import nums_dict")

nums_list = [i for i in range(1000000)]
print(f"{del_list1.timeit(number=1000):.10f}")

nums_list = [i for i in range(1000000)]
print(f"{del_list2.timeit(number=1000):.10f}")

nums_dict = {i: None for i in range(1000000)}
print(f"{del_dict1.timeit(number=1):.10f}")

nums_dict = {i: None for i in range(1000000)}
print(f"{del_dict2.timeit(number=1):.10f}")
