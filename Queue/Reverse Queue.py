def reverseQueue(queue):
  stack = []
  while len(queue) > 0:
    curr = queue.pop(0)
    stack.append(curr)
  while len(stack) > 0:
    curr = stack.pop()
    queue.append(curr)
  print(queue)

queue = list(map(int, input('Enter queue: ').split()))
reverseQueue(queue)