def linear_search(arr, item):
    n = len(arr)
    for i in range(n):
        if arr[i] == item:
            return i
    return -1

arr = list(map(int, input('Enter your array: ').split()))
item = int(input('Enter search item: '))
print(f'Item found at index {linear_search(arr, item)}')
