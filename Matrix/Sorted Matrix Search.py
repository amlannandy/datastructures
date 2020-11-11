from Common import inputMatrix

def searchSortedMatrix(matrix, item):
  x, y = len(matrix[0]) - 1, 0
  while x >= 0 and y < len(matrix):
    curr = matrix[x][y]
    if curr == item:
      print('Item present at [{}, {}]'.format(x, y))
      return
    elif curr < item:
      y += 1
    elif curr > item:
      x -= 1
  print('Item not found')

matrix = inputMatrix()
item = int(input('Enter search item: '))
searchSortedMatrix(matrix, item)