from Common import inputMatrix

arr = inputMatrix()
for i in range(len(arr)):
    if i % 2 == 0:
        for j in range(len(arr[0])):
            print(arr[i][j], end=' ')
    else:
        for j in reversed(range(len(arr[0]))):
            print(arr[i][j], end=' ')
    print()