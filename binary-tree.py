class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# node0 = Node(3)
# node1 = Node(4)
# node2 = Node(5)

# tree = node0
# node0.left = node1
# node0.right = node2

# print(node0.left.key)
# print(node0.right.key)

node0 = Node(2)
node1 = Node(3)
node2 = Node(5)
node3 = Node(1)
node4 = Node(3)
node5 = Node(7)
node6 = Node(4)
node7 = Node(6)
node8 = Node(8)

tree_tuple = ((1, 3, None), 2 , ((None, 3, 4), 5 , (6, 7, 8)))

def create_binary_tree(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = Node(data[1])
        node.left = create_binary_tree(data[0])
        node.right = create_binary_tree(data[2])
    elif data == None:
        node = None
    else:
        node = Node(data)
    return node

tree = create_binary_tree(tree_tuple)
print(tree.left.key, tree.right.key)

def tree_to_tuple(tree):
    pass

def display_keys():
    pass