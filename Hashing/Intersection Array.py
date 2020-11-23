def intersectionArray(arr1, arr2):
  dic = {}
  for a in arr1:
    if a in dic:
      dic[a] += 1
    else:
      dic[a] = 1
  res = []
  for a in arr2:
    if a in dic:
      res.append(a)
      if dic[a] == 1:
        del dic[a]
      else:
        dic[a] -= 1
  print(res)

arr1 = list(map(int, input('Enter Array 1: ').split()))
arr2 = list(map(int, input('Enter Array 2: ').split()))
intersectionArray(arr1, arr2)