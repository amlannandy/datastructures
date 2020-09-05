from Stack import Stack

stack = Stack()

string = input('Enter string: ')
for s in string:
    if s == ')' and stack.peek() == '(':
        stack.pop()
    elif s == ']' and stack.peek() == '[':
        stack.pop()
    elif s == '}' and stack.peek() == '{':
        stack.pop()
    else:
        stack.push(s)
print(stack.isEmpty())
