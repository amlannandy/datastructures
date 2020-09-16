def previousGreater(arr):
    size = len(arr)
    for i in range(size):
        found = False
        for j in reversed(range(0, i)):
            print("index {}".format(j))
            if arr[j] > arr[i]:
                print(arr[j], end=' ')
                found = True
                break
        if not found:
            print(-1, end=' ')


previousGreater([15, 10, 18, 12, 4, 6, 2, 8])
