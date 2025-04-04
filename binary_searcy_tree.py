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