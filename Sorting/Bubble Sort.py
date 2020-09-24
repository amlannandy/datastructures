def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


n = int(input('Enter size of Array: '))
print(f'Enter {n} elements: ')
arr = list(map(int, input().split()))
bubbleSort(arr)
print('Sorted Array is:')
print(arr)
