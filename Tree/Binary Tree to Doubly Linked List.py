from Node import Node

class ToDoublyLinkedList():
    def __init__(self):
        self.prev = None

    def to_linked_list(self, root):
        if not root:
            return root
        head = self.to_linked_list(root.left)
        if not self.prev:
            head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        self.to_linked_list(root.right)
        return head

def print_linked_list(head):
    curr = head
    while curr is not None:
        print('->', curr.val, end=' ')
        curr = curr.right

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = ToDoublyLinkedList()
head = sol.to_linked_list(root)
print_linked_list(head)