def linear_search(arr, item):
  n = len(arr)
  for i in range(n):
    if arr[i] == item:
      return True
  return False

n = int(input('Enter size of Array: '))
arr = list(map(int, input('Enter Array elements: ').split()))[:n]
item = int(input('Enter search item: '))
print(linear_search(arr, item))