def getFreq(arr):
  dic = {}
  for a in arr:
    if a in dic:
      dic[a] += 1
    else:
      dic[a] = 1
  for d in dic.items():
    print(d[0], '-', d[1], 'times')

arr = list(map(int, input('Enter Array: ').split()))
getFreq(arr)