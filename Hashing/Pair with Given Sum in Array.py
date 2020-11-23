def findPair(arr, target):
  dic = {}
  for a in arr:
    if target-a in dic:
      return True
    dic[a] = 1
  return False

arr = list(map(int, input('Enter Array: ').split()))
target = int(input('Enter target: '))
print(findPair(arr, target))