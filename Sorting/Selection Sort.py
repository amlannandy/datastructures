def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_pos = i
        for j in range(min_pos, n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        temp = arr[min_pos]
        arr[min_pos] = arr[i]
        arr[i] = temp


n = int(input('Enter size of Array: '))
print(f'Enter {n} elements: ')
arr = list(map(int, input().split()))
selectionSort(arr)
print('Sorted Array is:')
print(arr)
