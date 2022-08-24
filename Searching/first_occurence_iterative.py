def first_occurence_iterative(arr, item):
  beg, end = 0, len(arr)
  while beg <= end:
    mid = (beg + end)//2
    if item > arr[mid]:
      beg = mid + 1
    elif item < arr[mid]:
      end = mid - 1
    else:
      if mid == 0 or arr[mid - 1] != arr[mid]:
        return mid
      else:
        end = mid - 1
  return -1

n = int(input('Enter size of Array: '))
arr = list(map(int, input('Enter Array elements: ').split()))[:n]
item = int(input('Enter search item: '))
print(first_occurence_iterative(arr, item))