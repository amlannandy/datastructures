def evaluatePostFix(S):
  stack = []
  for s in S:
    if s.isdigit():
      stack.append(s)
    else:
      b = int(stack.pop())
      a = int(stack.pop())
      res = 0
      if s == '+':
        res = a + b
      elif s == '-':
        res = a - b
      elif s == '*':
        res = a * b
      else:
        res = a//b
      stack.append(str(res))
  return ''.join(stack)


s = input('Enter postfix expression: ')
print(evaluatePostFix(s))