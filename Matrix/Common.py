def inputMatrix():
    m = int(input('Enter number of rows: '))
    n = int(input('Enter number of columns: '))
    arr = []
    for i in range(m):
        row = list(map(int, input('Enter row {}: '.format(i+1)).split()))[:n]
        arr.append(row)
    return arr