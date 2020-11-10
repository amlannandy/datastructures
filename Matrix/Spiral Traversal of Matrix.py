from Common import inputMatrix

def spiralTraversal(arr):
    m, n = len(arr), len(arr[0])
    top, right, bottom, left = 0, n - 1, m - 1, 0
    res = []
    while top <= bottom and left <= right:
        print(top, right, bottom, left)
        # Top row
        res.extend(arr[top][left:right+1])
        # Right column
        for i in range(top+1, bottom):
            res.append(arr[i][right])
        # Bottom row
        if top < bottom:
            res.extend(arr[bottom][left:right+1][::-1])
        # Right wow
        if left < right:
            for i in reversed(range(top + 1, bottom)):
                res.append(arr[i][left])
        top += 1
        left += 1
        bottom -= 1
        left += 1
    return res

arr = inputMatrix()
res = spiralTraversal(arr)
print(res)