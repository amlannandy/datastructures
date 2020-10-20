def last_occurence(arr, item):
    beg, end, n = 0, len(arr) - 1, len(arr) - 1
    while beg <= end:
        mid = (beg + end)//2
        if arr[mid] == item:
            if mid != n and arr[mid + 1] == item:
                beg = mid + 1
            else:
                return mid
        elif arr[mid] < item:
            beg = mid + 1
        elif arr[mid] > item:
            end = mid - 1
    return -1

arr = list(map(int, input('Enter array: ').split()))
item = int(input('Enter item: '))
print(f'Last occurence is at {last_occurence(arr, item)}')