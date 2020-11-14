def searchRotatedArray(arr, item):
    beg, end = 0, len(arr) - 1
    while beg <= end:
        mid = (beg + end)//2
        if arr[mid] == item:
            return mid
        # when left side is sorted
        elif arr[beg] <= arr[mid]:
            if item >= arr[beg] and item < arr[mid]:
                end = mid - 1
            else:
                beg = mid + 1
        else:
            if item <= arr[end] and item > arr[mid]:
                beg = mid + 1
            else:
                end = mid - 1
    return -1

arr = list(map(int, input('Enter Array: ').split()))
item = int(input('Enter item: '))
print(f'Item is at index {searchRotatedArray(arr, item)}')