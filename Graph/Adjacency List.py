class AdjacencyList:
  def __init__(self, v):
    self.v = v
    self.arr = [-1] * v

  def addEdge(self, start, end):
    if start >= v or end >= v:
      return
    if self.arr[start][0] == -1:
      self.arr[start][0] = end
    else:
      self.arr[start].append(end)
    if self.arr[end][0] == -1:
      self.arr[end][0] = start
    else:
      self.arr[end].append(start)

  def deleteEdge(self, start, end):
    if start >= v or end >= v:
      return
    try:
      self.arr[start].remove(end)
    except ValueError:
      return
    try:
      self.arr[end].remove(start)
    except ValueError:
      return

  def display(self):
    for i, arr in self.arr:
      print(i, '->', arr)

  def printInstructions(self):
    print('GRAPH COMMANDS')
    print('1. ADD EDGE')
    print('2. DELETE EDGE')
    print('3. DISPLAY')
    print('4. EXIT')

size = int(input('Enter size: '))
adjList = AdjacencyList(size)

while True:
  choice = int(input("Enter command [0 for List]: "))
  if choice == 0:
    adjList.printInstructions()
  elif choice == 1:
    start = int(input('Enter start point: '))
    end = int(input('Enter end point: '))
    adjList.addEdge(start, end)
  elif choice == 2:
    start = int(input('Enter start point: '))
    end = int(input('Enter end point: '))
    adjList.deleteEdge(start, end)
  
