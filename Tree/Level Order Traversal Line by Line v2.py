from Node import Node

def line_by_line(root):
    if not root:
        return
    queue = [root]
    while len(queue) > 0:
        count = len(queue)
        for i in range(count):
            curr = queue.pop(0)
            print(curr.val, end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print()
    
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

line_by_line(root)