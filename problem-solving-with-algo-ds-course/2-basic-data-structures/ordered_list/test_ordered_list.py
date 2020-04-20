from models.ordered_list import OrderedList

ol = OrderedList()
ol.add(2)
ol.add(3)
ol.add(1)
ol.add(10)
ol.add(99)
ol.add(4)


print(ol.to_list())

print(ol.search(2))
ol.remove(3)
print(ol.to_list())
ol.remove(99)
print(ol.to_list())
ol.remove(1)
ol.remove(2)
ol.remove(4)
ol.remove(10)
print(ol.to_list())
