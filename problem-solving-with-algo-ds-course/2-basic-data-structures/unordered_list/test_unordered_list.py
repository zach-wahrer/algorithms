import unittest
from models.unordered_list import UnorderedList

ul = UnorderedList()
ul.add('test1')
ul.add('test2')
ul.add('test3')
ul.add('test4')
ul.append('Append at end1')
ul.add('test5')
ul.insert(2, 'insert in pos2')
ul.insert(0, 'insert in pos0')
ul.append('Append at end2')

print(ul.index('test4'))
print(ul.index('Append at end1'))

print(ul.to_list())

print(ul.pop(2))
print(ul.pop(0))

print(ul.to_list())
print('Length: ', len(ul))
print(ul.pop(6))
print('Length: ', len(ul))
ul.append('append at new tail')
print(ul.to_list())
