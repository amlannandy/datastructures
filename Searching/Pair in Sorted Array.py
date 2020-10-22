def find_pair(arr, target):
    left, right = 0, len(arr) - 1
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
if find_pair(arr, target):
    print('Exists')
else:
    print('Doesn\'t exist')