def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


n = int(input('Enter size of Array: '))
print(f'Enter {n} elements:')
arr = list(map(int, input().split()))
reverseArray(arr)
print('Reversed Array is: ')
print(arr)
