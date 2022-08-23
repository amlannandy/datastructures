def first_occurence(arr, item):
  for i in range(len(arr)):
    if arr[i] == item:
      return i
  return -1

n = int(input('Enter size of Array: '))
arr = list(map(int, input('Enter Array elements: ').split()))[:n]
item = int(input('Enter search item: '))
print(first_occurence(arr, item))