from Node import Node

def construct_tree_from_postorder(inorder, postorder):
    if not inorder:
        return None
    root = Node(postorder.pop())
    root_index = inorder.index(root.val)
    root.right = construct_tree_from_postorder(inorder[root_index + 1:], postorder)
    root.left = construct_tree_from_postorder(inorder[:root_index], postorder)
    return root