from collections import Counter

def getUniqueElements(nums, m):
  if not nums:
    return 0
  c = Counter(nums)
  r = list(reversed(c.most_common()))
  arr = []
  for i in r:
    arr.extend([i[0]] * i[1])
  index = 0
  while index < m:
    arr.pop(0)
    index += 1
  return len(set(arr))
  
arr = list(map(int, input('Enter Array: ').split()))
m = int(input('Enter no. of deletions: '))
print(getUniqueElements(arr, m))
  