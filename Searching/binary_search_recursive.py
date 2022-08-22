def binary_search_recursive(arr, item, beg, end):
  if beg > end:
    return -1
  mid = (beg + end)//2
  if item == arr[mid]:
    return mid
  elif item > arr[mid]:
    return binary_search_recursive(arr, item, mid + 1, end)
  else:
    return binary_search_recursive(arr, item, beg, mid - 1)

n = int(input('Enter size of Array: '))
arr = list(map(int, input('Enter Array elements: ').split()))[:n]
item = int(input('Enter search item: '))
print(binary_search_recursive(arr, item, 0, n-1))