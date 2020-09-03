from Stack import Stack


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
