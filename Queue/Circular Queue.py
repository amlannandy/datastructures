class CircularQueue:
    def __init__(self, k: int):
        self.front = 0
        self.rear = -1
        self.queue = [0] * k
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = 0
            self.rear = -1
            return True
        if self.front == self.size - 1:
            self.front = 0
            return True
        self.front += 1
        return True
        
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        if self.rear == -1 and self.front == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.front == 0 and self.rear == self.size - 1:
            return True
        if not self.isEmpty() and self.rear == self.front - 1:
            return True
        return False

    def print(self) -> None:
        if self.isEmpty():
            return
        if self.rear >= self.front:
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=' ')
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end= ' ')
            for i in range(self.rear + 1):
                print(self.queue[i], end=' ')
        print()

    def getSize(self) -> int:
        if self.isFull():
            return self.size
        if self.isEmpty():
            return 0
        if self.rear < self.front:
            return self.front - self.rear - 1
        return self.rear - self.front + 1

    def currentSructure(self):
        print(self.queue)



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


queue = CircularQueue(5)

while True:
    choice = int(input('Enter your command: [0 for Commands List]: '))
    if choice == 0:
        printInstructions()
    elif choice == 1:
        item = int(input('Enter item: '))
        queue.enQueue(item)
    elif choice == 2:
        queue.deQueue()
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
