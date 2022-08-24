def first_occurence_recursive(arr, item, beg, end):
  if beg > end:
    return -1
  mid = (beg + end)//2
  if item > arr[mid]:
    return first_occurence_recursive(arr, item, mid + 1, end)
  elif item < arr[mid]:
    return first_occurence_recursive(arr, item, beg, mid - 1)
  else:
    if mid == 0 or arr[mid-1] != arr[mid]:
      return mid
    else:
      return first_occurence_recursive(arr, item, beg, mid - 1)

n = int(input('Enter size of Array: '))
arr = list(map(int, input('Enter Array elements: ').split()))[:n]
item = int(input('Enter search item: '))
print(first_occurence_recursive(arr, item, 0, n - 1))