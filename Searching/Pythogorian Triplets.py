def find_pythagoras_triplets(arr):
    n = len(arr)
    for i in range(n):
        curr = arr[i] ** 2
        if find_pair(arr, curr):
            return True
    return False

def find_pair(arr, target):
    left, right = 0, len(arr)-1
    while left < right:
        curr = arr[left] ** 2 + arr[right] ** 2
        if curr == target:
            return True
        elif curr < target:
            left += 1
        else:
            right -= 1
    return False

arr = list(map(int, input('Enter Array: ').split()))
if find_pythagoras_triplets(arr):
    print('Pythagorian Triplets exist')
else:
    print('Pythagorian Triplets don\'t exist')