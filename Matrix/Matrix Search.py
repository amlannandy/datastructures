from Common import inputMatrix

def searchMatrix(matrix, item):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == item:
        print('Item found at [{}, {}]'.format(i, j))
        return
  print('Item not found')

matrix = inputMatrix()
item = int(input('Enter search item: '))
searchMatrix(matrix, item)