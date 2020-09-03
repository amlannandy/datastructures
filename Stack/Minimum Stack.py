class MinStack():

    def __init__(self):
        self.top = -1
        self.stack = []
        self.min = []

    def push(self, item):
        self.stack.append(item)
        if self.top == -1 or item < self.min[self.top]:
            self.min.append(item)
        else:
            self.min.append(self.min[self.top])
        self.top += 1

    def display(self):
        if self.isEmpty():
            return
        else:
            print(self.stack)

    def isEmpty(self):
        if self.top == -1:
            print('Stack underflow')
            return True
        else:
            return False

    def getMin(self):
        if self.isEmpty():
            return None
        else:
            return self.min[self.top]


def printInstructions():
    print('Command List')
    print('1. Push')
    print('2. Pop')
    print('3. Minimum')
    print('4. Display')
    print('5. Exit')


stack = MinStack()

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
        print(f'Minimum is {stack.getMin()}')
    elif choice == 4:
        stack.display()
    elif choice == 5:
        break
