class AdjacencyList:
  def __init__(self, size):
    self.size = size
    self.arr = [[] for i in range(size)]

  def insert(self, u, v):
    self.arr[u].append(v)
    self.arr[v].append(u)

  def display(self):
    for index, list in enumerate(self.arr):
      print(index, end='-> ')
      for item in list:
        print(item, end=' ')
      print()
  
list = AdjacencyList(5)
list.insert(0, 1)
list.insert(0, 2)
list.insert(3, 4)
list.display()