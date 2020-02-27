from models.binary_tree import BinaryTree

# tree = BinaryTree('a')
#
# print(tree.get_root_val())
# print(tree.get_left_child())
#
# tree.insert_left('b')
#
# print(tree.get_left_child())
# print(tree.get_left_child().get_root_val())
#
# tree.insert_right('c')
#
# print(tree.get_right_child())
# print(tree.get_right_child().get_root_val())
#
# tree.get_right_child().set_root_val('hello')
#
# print(tree.get_right_child().get_root_val())

tree = BinaryTree('a')
tree.insert_left('b')
tree.insert_right('c')
tree.get_left_child().insert_right('d')
tree.get_right_child().insert_left('e')
tree.get_right_child().insert_right('f')

print(tree.get_root_val())
print(tree.get_left_child().get_root_val())
print(tree.get_left_child().get_right_child().get_root_val())
