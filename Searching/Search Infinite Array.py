def binary_search(arr, item, beg, end):
    while beg <= end:
        mid = (beg + end)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            beg = mid + 1
        elif arr[mid] > item:
            end = mid - 1
    return -1

def search_infinite_array(arr, item):
    if arr[0] == item:
        return 0
    i = 1
    while arr[i] < item:
        i *= 2
    if arr[i] == item:
        return i
    return binary_search(arr, item, i//2 + 1, i - 1)

arr = list(map(int, input('Enter array: ').split()))
item = int(input('Enter item: '))
print(f'Item is at index {search_infinite_array(arr, item)}')