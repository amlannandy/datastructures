def findSubArray(arr):
  dic = {}
  pre_sum = 0
  for a in arr:
    pre_sum += a
    if pre_sum in dic:
      return True
    if pre_sum == 0:
      return True
    dic[pre_sum] = 1
  return False

arr = list(map(int, input('Enter Array: ').split()))
print(findSubArray(arr))