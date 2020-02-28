from models.bst import BinarySearchTree

tree = BinarySearchTree()
tree[3] = 'a'
tree[4] = 'b'
tree[6] = 'c'
tree[2] = 'd'

for i in tree:
    print(tree[i])

print(2 in tree)
