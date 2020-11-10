from Common import inputMatrix

arr = inputMatrix()
for row in arr:
    for item in row:
        print(item, end=' ')
    print()