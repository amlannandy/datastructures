from Common import inputMatrix

def getBoundary(arr):
    m = len(arr)
    n = len(arr[0])
    res = []
    last = []
    for i in range(m):
        if i == 0:
            res.extend(arr[i])
        elif i == m - 1:
            res.extend(arr[i][::-1])
        else:
            res.append(arr[i][-1])
            if n > 1:
                last.insert(0, arr[i][0])
    res.extend(last)
    return res

arr = inputMatrix()
res = getBoundary(arr)
for el in res:
    print(el, end=' ')
