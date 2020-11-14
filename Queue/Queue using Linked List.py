class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, val):
        node = Node(val)
        if self.isEmpty():
            self.head = node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

    def dequeue(self):
        if self.isEmpty():
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next

    def print(self):
        if self.isEmpty():
            return
        curr = self.head
        while curr is not None:
            print(curr.val, end=' ')
            curr = curr.next
        print()

    def isEmpty(self):
        if self.head is None:
            print("Queue Empty")
            return True
        else:
            return False


def printInstructions():
    print('Command List')
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Print')
    print('4. Exit')


queue = Queue()

while True:
    choice = int(input('Enter your command: [0 for Commands List]: '))
    if choice == 0:
        printInstructions()
    elif choice == 1:
        item = int(input('Enter item: '))
        queue.enqueue(item)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.print()
    elif choice == 4:
        break
