def peak_element(arr):
    beg, end, n = 0, len(arr) - 1, len(arr)
    while beg <= end:
        mid = (beg + end)//2
        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            return mid
        if mid > 0 and arr[mid - 1] >= arr[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

arr = list(map(int, input('Enter Array: ').split()))
print(f'Peak element is at index {peak_element(arr)}')