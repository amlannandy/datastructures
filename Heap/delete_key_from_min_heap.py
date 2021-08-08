class MinHeap:
  def __init__(self, max_size):
    self.size = 0
    self.max_size = max_size
    self.arr = [None] * max_size
    
  def parent(self, i):
    return (i-1)//2
    
  def left_child(self, i):
    return 2 * i + 1
    
  def right_child(self, i):
    return 2 * i + 2
    
  def is_leaf(self, i):
    return i < self.size and i >= self.size//2
    
  def insert(self, val):
    self.arr[self.size] = val
    self.heapify(self.size)
    self.size += 1
    
  def heapify(self, i):
    while i != 0 and self.arr[i] < self.arr[self.parent(i)]:
      self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
      i = self.parent(i)
      
  def delete_key(self, i):
    if i >= self.size:
      return
    self.arr[i] = -1
    self.heapify(i)
    self.arr[0] = self.arr[self.size - 1]
    self.size -= 1
    self.min_heapify(0)
    
  def min_heapify(self, i):
    if self.is_leaf(i):
      return
    left_child = self.left_child(i)
    right_child = self.right_child(i)
    
    if right_child < self.size:
      if self.arr[i] <= self.arr[left_child] and self.arr[i] <= self.arr[right_child]:
        return
    else:
      if self.arr[i] <= self.arr[left_child]:
        return
      
    smallest = i
    if left_child < self.size and self.arr[left_child] < self.arr[smallest]:
      smallest = left_child
    if right_child < self.size and self.arr[right_child] < self.arr[smallest]:
      smallest = right_child
    if i != smallest:
      self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
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
    n, k = map(int, input().split())
    k -= 1
    arr = list(map(int, input().split()))
    heap = MinHeap(n)
    for a in arr:
      heap.insert(a)
    heap.delete_key(k)
    heap.print_heap()
except Exception as err:
  print(err)