from SinglyLinkedListNode import Node

class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,item):
        node = Node(item)
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insertAtEnd(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def insertAfterNode(self, item, value):
        node = Node(item)
        if not self.head:
            return
        curr = self.head
        while curr is not None and curr.val != value:
            curr = curr.next
        if not curr:
            return
        node.next = curr.next
        curr.next = node

    def insertBeforeNode(self, item, value):
        node = Node(item)
        if not self.head:
            return
        if self.head.val == value:
            node.next = self.head
            self.head = node
        curr = self.head
        prev = curr
        while curr is not None and curr.val != value:
            prev = curr
            curr = curr.next
        if not curr:
            return
        prev.next = node
        node.next = curr

    def deleteAtBeginning(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def deleteParticularNode(self, item):
        if not self.head:
            return
        if not self.head.next:
            if self.head.val == item:
                self.head = None
            return
        curr = self.head
        prev = self.head
        while curr is not None and curr.val != item:
            prev = curr
            curr = curr.next
        if not curr:
            return
        prev.next = curr.next

    def display(self):
        if not self.head:
            return
        curr = self.head
        while curr is not None:
            print(curr.val, end=' ')
            curr = curr.next
        print()

def printInstructions():
    print('1. Insert at Beginning')
    print('2. Insert at End')
    print('3. Insert after Node')
    print('4. Insert before Node')
    print('5. Delete from Beginning')
    print('6. Delete from End')
    print('7. Delete particular node')
    print('8. Display Linked List')
    print('9. Exit')

ll = SinglyLinkedList()
while True:
    choice = int(input('Enter your command [Enter 0 for Commands List]: '))
    if choice == 0:
        printInstructions()
    elif choice == 1:
        item = int(input('Enter item: '))
        ll.insertAtBeginning(item)
    elif choice == 2:
        item = int(input('Enter item: '))
        ll.insertAtEnd(item)
    elif choice == 3:
        value = int(input('Enter node after which item is to be inserted: '))
        item = int(input('Enter item: '))
        ll.insertAfterNode(item, value)
    elif choice == 4:
        value = int(input('Enter node before which item is to be inserted: '))
        item = int(input('Enter item: '))
        ll.insertBeforeNode(item, value)
    elif choice == 5:
        ll.deleteAtBeginning()
    elif choice == 6:
        ll.deleteAtEnd()
    elif choice == 7:
        item = int(input('Enter item: '))
        ll.deleteParticularNode(item)
    elif choice == 8:
        ll.display()
    else:
        break