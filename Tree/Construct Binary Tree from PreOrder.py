from Node import Node

def construct_tree_from_preorder(preorder, inorder):
    if not inorder:
        return None
    root = Node(preorder.pop(0))
    root_index = inorder.index(root.val)
    root.left = construct_tree_from_preorder(preorder, inorder[:root_index])
    root.right = construct_tree_from_preorder(preorder, inorder[root_index + 1:])
    return root