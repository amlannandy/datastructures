def no_of_occurences(arr, item):
    first = first_occurence(arr, item)
    if first == -1:
        return 0
    else:
        return last_occurence(arr, item) - first + 1

def first_occurence(arr, item):
    beg, end = 0, len(arr) - 1
    while beg <= end:
        mid = (beg + end)//2
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

arr = list(map(int, input('Enter Array: ').split()))
item = int(input('Enter item: '))
print(f'No of occurences of {item} is {no_of_occurences(arr, item)}')