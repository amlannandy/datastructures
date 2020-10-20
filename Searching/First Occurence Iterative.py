def first_occurence(arr, item):
    beg, end = 0, len(arr) - 1
    while beg <= end:
        mid = (beg + end) // 2
        if arr[mid] == item:
            if mid != 0 and arr[mid-1] == item:
               end = mid - 1
            else:
                return mid
        elif arr[mid] < item:
            beg = mid + 1
        elif arr[mid] > item:
            end = mid - 1
    return -1

arr = list(map(int, input('Enter array: ').split()))
item = int(input('Enter search item: '))
print(f'First occurence is {first_occurence(arr, item)}.')