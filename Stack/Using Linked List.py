class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.top = -1
        self.head = None

    def push(self, val):
        node = Node(val)
        if self.head is None:
            self.top += 1
            self.head = node
            return
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.top -= 1
            return
        self.head = self.head.next
        self.top -= 1

    def peek(self):
        if self.head is None:
            return None
        return self.head.val

    def size(self):
        return self.top + 1

    def display(self):
        if self.head is None:
            return
        curr = self.head
        while curr is not None:
            print(curr.val, end=" ")
            curr = curr.next


def printInstructions():
    print('Command List')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')


stack = Stack()

while True:
    choice = int(input('Enter your command: [0 for Commands List]'))
    if choice == 0:
        printInstructions()
    elif choice == 1:
        item = int(input('Enter item: '))
        stack.push(item)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        print(f'Item on top is {stack.peek()}')
    elif choice == 4:
        stack.display()
    elif choice == 5:
        break
