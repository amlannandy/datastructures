def countDistinct(arr):
  s = set()
  for a in arr:
    s.add(a)
  return len(s)

arr = list(map(int, input('Enter Array: ').split()))
print('Number of distinct elements is', countDistinct(arr))