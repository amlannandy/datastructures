def binarySearch(arr, item):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end)//2
        if item == arr[mid]:
            return mid
        if item < arr[mid]:
            end = mid
        elif item > arr[mid]:
            beg = mid + 1
    return -1


n = int(input('Enter size of Array: '))
print(f'Enter {n} elements:')
arr = list(map(int, input().split()))
item = int(input('Enter search item: '))
index = binarySearch(arr, item)
print(f'Item is at index {index}')
