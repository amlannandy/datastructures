def linearSearch(arr, item):
    for i, a in enumerate(arr):
        if arr[i] == item:
            return i
    return -1


n = int(input('Enter size of Array: '))
arr = []
print(f'Enter {n} elements:')
for i in range(n):
    arr.append(int(input()))
item = int(input('Enter search item: '))
index = linearSearch(arr, item)
print(f'Item is at index {index}')
