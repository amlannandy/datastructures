class Stack:

    def __init__(self):
        self.top = -1
        self.stack = []

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return
        else:
            self.stack.pop()
            self.top -= 1

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.stack[self.top]

    def display(self):
        if self.isEmpty():
            return
        else:
            print(self.stack)

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
