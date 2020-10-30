from Node import Node

def level_order_traversal(root):
    if not root:
        return
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr.val, end=' ')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

level_order_traversal(root)