def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    k = 0
    arr3 = [0] * (m+n)
    for i in range(m):
        arr3[k] = arr1[i]
        k += 1
    for j in range(n):
        arr3[k] = arr2[j]
        k += 1
    return arr3


m = int(input('Enter size of Array 1: '))
print(f'Enter {m} elements:')
arr1 = list(map(int, input().split()))
n = int(input('Enter size of Array 2: '))
print(f'Enter {n} elements:')
arr2 = list(map(int, input().split()))
print('Merged Array is:')
res = merge(arr1, arr2)
print(res)
