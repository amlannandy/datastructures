def binary_search(arr, item):
    beg, end = 0, len(arr) - 1
    while beg <= end:
        mid = (beg + end)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            beg = mid + 1
        elif arr[mid] > item:
            end = mid
    return -1

arr = list(map(int, input('Enter your array: ').split()))
item = int(input('Enter search item: '))
print(f'Item found at index {binary_search(arr, item)}')