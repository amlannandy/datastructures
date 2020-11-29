def findSubArray(arr, k):
  dic = {}
  pre = 0
  for a in arr:
    pre += a
    if (pre - k) in dic:
      return True
    if pre == k:
      return True
    dic[pre] = 1
  return True

arr = list(map(int, input('Enter Array: ').split()))
k = int(input('Enter k: '))
print(findSubArray(arr, k))