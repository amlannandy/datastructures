def first_occurence(arr, item, beg, end):
    if beg > end:
        return -1
    mid = (beg + end)//2
    if arr[mid] == item:
        if mid != 0 and arr[mid - 1] == item:
            return first_occurence(arr, item, beg, mid - 1)
        else:
            return mid
    elif arr[mid] < item:
        return first_occurence(arr, item, mid+1, end)
    elif arr[mid] > item:
        return first_occurence(arr, item, beg, mid - 1)

arr = list(map(int, input('Enter array: ').split()))
item = int(input('Enter search item: '))
print(f'First occurence is {first_occurence(arr, item, 0, len(arr) - 1)}.')