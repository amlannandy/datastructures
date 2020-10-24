def find_majority(arr):
    res, count = 0, 1
    n = len(arr)
    for i in range(1, n):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1
    count = 0
    for i in range(n):
        if arr[i] == arr[res]:
            count += 1
    if count <= n//2:
        return -1
    return res

arr = list(map(int, input('Enter array: ').split()))
print(f'Majority element in array is {find_majority(arr)}')