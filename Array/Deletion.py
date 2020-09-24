def delete(arr, pos):
    n = len(arr)
    for i in range(pos, n-1):
        arr[i] = arr[i+1]
    arr.pop()


n = int(input('Enter size of Array: '))
arr = list(map(int, input().split()))
pos = int(input('Enter position of item to delete: '))
delete(arr, pos)
print(arr)
