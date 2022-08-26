def last_occurence_naive(arr, item):
  n = len(arr)
  for i in range(n):
    if arr[i] == item:
      if i == n - 1 or arr[i+1] != arr[i]:
        return i
  return -1

n = int(input('Enter size of Array: '))
arr = list(map(int, input('Enter Array elements: ').split()))[:n]
item = int(input('Enter search item: '))
print(last_occurence_naive(arr, item))