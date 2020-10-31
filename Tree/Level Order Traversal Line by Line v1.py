from Node import Node

def travel_line(root):
    if not root:
        return
    queue = [root, None]
    while len(queue) > 1:
        curr = queue.pop(0)
        if not curr:
            print()
            queue.append(None)
        else:
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

travel_line(root)