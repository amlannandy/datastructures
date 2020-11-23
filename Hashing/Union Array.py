def getUnion(arr1, arr2):
  res = set()
  for a in arr1:
    res.add(a)
  for a in arr2:
    res.add(a)
  print(res)

arr1 = list(map(int, input('Enter Array 1: ').split()))
arr2 = list(map(int, input('Enter Array 2: ').split()))
getUnion(arr1, arr2)