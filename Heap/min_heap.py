class MinHeap:
  def __init__(self, max_size):
    self.max_size = max_size
    self.size = 0
    self.arr = [None] * max_size
    
  def parent(self, i):
    return (i-1)//2
    
  def left(self, i):
    return 2 * i + 1
    
  def heapify(self, i):
    while i != 0 and self.arr[i] < self.arr[self.parent(i)]:
      self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
      i = self.parent(i)
  
  def insert(self, val):
    self.arr[self.size] = val
    self.heapify(self.size)
    self.size += 1
    
  def print_heap(self):
    if self.size == 0:
      return
    for i in range(self.size):
      print(self.arr[i], end=' ')
    print()
    
T = int(input())
for t in range(T):
  n = int(input())
  arr = list(map(int, input().split()))
  heap = MinHeap(n)
  for a in arr:
    heap.insert(a)
  heap.print_heap()