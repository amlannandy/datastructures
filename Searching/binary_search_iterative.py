def binary_search_iterative(arr, item):
  beg, end = 0, len(arr) - 1
  while beg <= end:
    mid = (beg + end)//2
    if item == arr[mid]:
      return mid
    elif item > arr[mid]:
      beg = mid + 1
    else:
      end = mid - 1
  return -1

n = int(input('Enter size of Array: '))
arr = list(map(int, input('Enter Array elements: ').split()))[:n]
item = int(input('Enter search item: '))
print(binary_search_iterative(arr, item))