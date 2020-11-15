def generateNums(nums, size):
  queue = []
  res = []
  for n in nums:
    queue.append(n)
  while len(res) < size:
    curr = queue.pop(0)
    for n in nums:
      queue.append(curr + n)
    res.append(int(curr))
  print(res)

nums = list(map(str, input('Enter your set: ').split()))
size = int(input('Enter no. of results you want: '))
generateNums(nums, size)
