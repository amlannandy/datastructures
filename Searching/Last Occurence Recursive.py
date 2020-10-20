def last_occurence(arr, item, n, beg, end):
    if beg > end:
        return -1
    mid = (beg + end)//2
    if arr[mid] == item:
        if mid != n - 1 and arr[mid + 1] == item:
            return last_occurence(arr, item, n, mid + 1, end)
        else:
            return mid
    elif arr[mid] < item:
        return last_occurence(arr, item, n, mid + 1, end)
    elif arr[mid] > item:
        return last_occurence(arr, item, n, beg, mid - 1)

arr = list(map(int, input('Enter array: ').split()))
item = int(input('Enter item: '))
print(f'Last occurence is at {last_occurence(arr, item, len(arr), 0, len(arr) - 1)}')