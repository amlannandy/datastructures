class MinHeap:
  
  def __init__(self, max_size):
    self.max_size = max_size
    self.arr = [None] * max_size
    self.size = 0
    
  def parent(self, i):
    return (i-1)//2
    
  def left_child(self, i):
    return 2 * i + 1
    
  def right_child(self, i):
    return 2 * i + 2
    
  def is_leaf(self, index):
    i = self.size // 2
    return index >= i and index <= self.size - 1
    
  def insert(self, val):
    self.arr[self.size] = val
    self.heapify_up(self.size)
    self.size += 1
    
  def heapify_up(self, i):
    while i != 0 and self.arr[i] < self.arr[self.parent(i)]:
      self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
      i = self.parent(i)
      
  def extract_min(self):
    if self.size == 0:
      return -1
    max_val = self.arr[0]
    self.arr[0] = self.arr[self.size - 1]
    self.size -= 1
    self.min_heapify(0)
    return max_val
    
  def min_heapify(self, index):
    if self.is_leaf(index):
      return
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    if right_child < self.size:
      if self.arr[index] <= self.arr[left_child] and self.arr[index] <= self.arr[right_child]:
        return
    else:
      if self.arr[index] <= self.arr[left_child]:
        return
    smallest = index
    if left_child < self.size and self.arr[left_child] < self.arr[smallest]:
      smallest = left_child
    if right_child < self.size and self.arr[right_child] < self.arr[smallest]:
      smallest = right_child
    if index != smallest:
      self.arr[index], self.arr[smallest] = self.arr[smallest], self.arr[index]
      self.min_heapify(smallest)
      
  def print_heap(self):
    if self.size == 0:
      return
    for i in range(self.size):
      print(self.arr[i], end=' ')
    print()
  
try:
  T = int(input())
  for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = MinHeap(n)
    for a in arr:
      heap.insert(a)
    min_val = heap.extract_min()
    print(min_val, end=' ')
    heap.print_heap()
except Exception as err:
  print(err)