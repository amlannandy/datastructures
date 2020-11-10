from Common import inputMatrix

arr = inputMatrix()

m = len(arr)
n = len(arr[0])
res = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        res[i][j] = arr[j][i]

for i in range(n):
    for j in range(m):
        print(res[i][j], end=' ')
    print()