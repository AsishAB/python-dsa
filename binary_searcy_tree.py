# BST - Binary Search Tree
# The left node contains all the nodes that are less than the Root Node
# The right node contains all the nodes that are greater than the Root Node

# Check if a tree is a Binary Search Tree. Also, return the Minimum Node and the Maximum Node


def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (
                    is_bst_l and is_bst_r and
                    (max_l is None or node.key > max_l) and
                    (min_r is None or node.key < min_r)
                   )

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key

def insert_node_in_bst(node, key,value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert_node_in_bst(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert_node_in_bst(node.right, key, value)
        node.right.parent = node

    return node

# Find a node in a BST

def find_node(node, key):
    if node is None:
        return None
    elif key == node.key:
        return node
    elif key < node.key:
        return find_node(node.left, key)
    elif key > node.key:
        return find_node(node.right, key)
    
# List all nodes in a BST
def list_all(node):
    if node is None:
        return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def make_balanced_bst(data, lo = 0, hi = None, parent= None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]
    # root = BSTNode(key, value) # Create this Class BSTNode  first
    root = None # Remove this after creating BSTNode
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid - 1, root)
    root.left = make_balanced_bst(data, mid + 1, hi, root)

    return root

# Function to balance an Unbalanced BST
# We already have a list of sorted data, just need to create the BST

def balance_bst(node):
    return make_balanced_bst(list_all(node))
    
