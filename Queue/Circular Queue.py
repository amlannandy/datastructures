class Queue:

    def __init__(self, size):
        self.queue = [0] * size
        self.rear = -1
        self.front = 0
        self.size = size

    def enqueue(self, item):
        if self.isFull():
            print('Queue Full')
            return
        if self.front != 0 and self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print('Queue Empty')
            return
        if self.front == self.rear:
            self.front = 0
            self.rear = 1
            return
        if self.front == self.size - 1:
            self.front = 0
            return
        self.front += 1

    def print(self):
        if self.isEmpty():
            print("Queue Empty")
            return
        if self.front <= self.rear:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=' ')
            for i in range(self.rear + 1):
                print(self.queue[i], end=' ')
        print()

    def getSize(self):
        if self.isEmpty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front
        else:
            return self.size - self.front + self.rear

    def currentSructure(self):
        print(self.queue)

    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self):
        return self.front == 0 and self.rear == -1

    def isFull(self):
        if self:
            return self.front == 0 and self.rear == self.size - 1


def printInstructions():
    print('Command List')
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. Front')
    print('4. Rear')
    print('5. Print')
    print('6. Size')
    print('7. Structure')
    print('8. Exit')


queue = Queue(5)

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
        print(f'Item in front is {queue.getFront()}')
    elif choice == 4:
        print(f'Item in rear is {queue.getRear()}')
    elif choice == 5:
        queue.print()
    elif choice == 6:
        print(f'Size is {queue.getSize()}')
    elif choice == 7:
        queue.currentSructure()
    elif choice == 8:
        break
