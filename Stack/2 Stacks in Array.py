class TwinStack:

    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, item):
        if self.isFull():
            return
        self.top1 += 1
        self.stack[self.top1] = item

    def push2(self, item):
        if self.isFull():
            return
        self.top2 -= 1
        self.stack[self.top2] = item

    def pop1(self):
        if self.top1 == -1:
            return
        self.top1 -= 1

    def pop2(self):
        if self.top2 == self.size:
            return
        self.top2 += 1

    def peek1(self):
        if self.top1 == -1:
            return None
        return self.stack[self.top1]

    def peek2(self):
        if self.top2 == self.size:
            return None
        return self.stack[self.top2]

    def display1(self):
        if self.top1 == -1:
            return
        for i in reversed(range(self.top1 + 1)):
            print(self.stack[i], end=" ")
        print()

    def display2(self):
        if self.top1 == -1:
            return
        for i in reversed(range(self.top2, self.size)):
            print(self.stack[i], end=" ")
        print()

    def displayFull(self):
        print(self.stack)

    def isFull(self):
        if self.top1 >= self.top2 - 1:
            return True
        else:
            return False


def printInstructions():
    print('Command List')
    print('1. Push 1')
    print('2. Push 2')
    print('3. Pop 1')
    print('4. Pop 2')
    print('5. Peek 1')
    print('6. Peek 2')
    print('7. Display 1')
    print('8. Display 2')
    print('9. Display Whole')
    print('10. Exit')


size = int(input("Input size of Array: "))
stack = TwinStack(size=size)
while True:
    choice = int(input('Enter your command: [0 for Commands List] '))
    if choice == 0:
        printInstructions()
    elif choice == 1:
        item = int(input('Enter item: '))
        stack.push1(item)
    elif choice == 2:
        item = int(input('Enter item: '))
        stack.push2(item)
    elif choice == 3:
        stack.pop1()
    elif choice == 4:
        stack.pop2()
    elif choice == 5:
        print(f'Item on top is {stack.peek1()}')
    elif choice == 6:
        print(f'Item on top is {stack.peek2()}')
    elif choice == 7:
        stack.display1()
    elif choice == 8:
        stack.display2()
    elif choice == 9:
        stack.displayFull()
    elif choice == 10:
        break
