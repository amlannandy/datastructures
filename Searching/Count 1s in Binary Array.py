def countOnes(arr):
    beg, end, size = 0, len(arr) - 1, len(arr)
    while beg <= end:
        mid = (beg + end)//2
        if arr[mid] == 1:
            if mid != 0 and arr[mid - 1] == 1:
                end = mid - 1
            else:
                return size - mid
        else:
            beg = mid + 1
    return 0

arr = list(map(int, input('Input Binary Array: ').split()))
print(f'Number of ones is {countOnes(arr)}')