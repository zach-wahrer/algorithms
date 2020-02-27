from models.bin_heap import BinHeap

heap = BinHeap()
heap.build_heap([11, 33, 1, 8, 9, 43, 100, 2])

print(heap.heap_list)

heap.insert(1000)
heap.insert(10)

print(heap.heap_list)

print(heap.del_min())

print(heap.heap_list)

heap2 = BinHeap()
heap2.build_heap(['a', 'x', 'y', 'z', 'r'])
print(heap2.heap_list)
