from Common import inputMatrix

def rotateMatrix(arr):
    m = len(arr)
    n = len(arr[0])
    res = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            res[n-i-1][j] = arr[j][i]
    return res

arr = inputMatrix()
res = rotateMatrix(arr)
for i in range(len(res)):
    for j in range(len(res[0])):
        print(res[i][j], end=' ')
    print()