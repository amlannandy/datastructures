class Stack:

  def __init__(self, size):
    self.size = size
    self.q1 = [0] * size
    self.q2 = [0] * size
    self.top = -1

  def push(self, val):
    if self.isFull():
      return
    while len(self.q1) > 0:
      curr = self.q1.pop(0)
      self.q2.append(curr)
    self.q1.append(val)
    while len(self.q2) > 0:
      curr = self.q2.pop(0)
      self.q1.append(curr)
    self.top += 1

  def pop(self):
    if self.isEmpty():
      return
    self.top -= 1

  def peek(self):
    if self.isEmpty():
      return -1
    return self.q1[self.top]

  def isEmpty(self):
    if self.top == -1:
      return True
    return False

  def isFull(self):
    if self.top == self.size - 1:
      return True
    return False

  def display(self):
    if self.isEmpty():
      return
    for i in range(self.top + 1):
      print(self.q1[i], end=' ')
    print()

def printInstructions():
    print('Command List')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')

stack = Stack(int(input('Enter size: ')))

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