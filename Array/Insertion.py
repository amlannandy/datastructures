def insert(arr, item, pos):
    n = len(arr)
    arr.append(0)
    for i in reversed(range(pos, n+1)):
        arr[i] = arr[i-1]
    arr[pos] = item


n = int(input('Enter size of Array: '))
print(f'Enter {n} elements:')
arr = list(map(int, input().split()))
item = int(input('Enter item: '))
pos = int(input('Enter position: '))
insert(arr, item, pos)
print('Updated Array is:')
print(arr)
