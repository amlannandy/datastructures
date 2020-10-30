from Node import Node

def preOrderTraversal(root: Node):
    if root is None:
        return
    print(root.val, end=' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def inOrderTraversal(root: Node):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.val, end=' ')
    inOrderTraversal(root.right)


def postOrderTraversal(root: Node):
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.val, end=' ')


head = Node(1)
head.left = Node(2)
head.left.left = Node(3)
head.left.right = Node(4)
head.right = Node(5)
head.right.left = Node(6)
head.right.right = Node(7)

print('Pre Order Traversal')
preOrderTraversal(head)
print('\nIn Order Traversal')
inOrderTraversal(head)
print('\nPost Order Traversal')
postOrderTraversal(head)
