def binary_search(arr, item, beg, end):
    if beg > end:
        return -1
    mid = (beg + end)//2
    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        return binary_search(arr, item, mid + 1, end)
    elif arr[mid] > item:
        return binary_search(arr, item, beg, mid - 1)

arr = list(map(int, input('Enter your array: ').split()))
item = int(input('Enter search item: '))
print(f'Item found at index {binary_search(arr, item, 0, len(arr))}')