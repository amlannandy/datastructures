def find_triplet(arr, target):
    n = len(arr)
    for i in range(n):
        if find_pair(arr, target - arr[i], i+1, n-1):
            return True
    return False

def find_pair(arr, target, left, right):
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return True
        elif curr < target:
            left += 1
        else:
            right -= 1
    return False

arr = list(map(int, input('Enter Array: ').split()))
target = int(input('Enter Target: '))
if find_triplet(arr, target):
    print('Exists')
else:
    print('Doesn\'t exist')