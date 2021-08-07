class MaxHeap:
  def __init__(self, max_size):
    self.max_size = max_size
    self.size = 0
    self.arr = [0] * max_size

  def insert(self, value):
    if self.size == self.max_size:
      print('Overflow')
      return
    self.arr[self.size] = value
    self.size += 1

  def build_heap(self):
    if self.size == 0:
      print('Underflow')
      return
    # We have to heapify only non-leaves
    # Non-leaves have index betwwen 0 and floor(size/2) - 1
    index = self.size // 2 - 1
    for i in reversed(range(0, index + 1)):
      self.max_heapify(i)

  def max_heapify(self, index):
    if self.is_leaf(index):
      return
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    # Check if node is already max
    if right_child < self.size:
      # Right child exists
      if self.arr[index] >= self.arr[left_child] and self.arr[index] >= self.arr[right_child]:
        return
    else:
      # right child does not exist
      if self.arr[index] >= self.arr[left_child]:
        return
    # Swap max value to node
    largest = index
    if left_child < self.size and self.arr[left_child] > self.arr[largest]:
      largest = left_child
    if right_child < self.size and self.arr[right_child] > self.arr[largest]:
      largest = right_child
    if index != largest:
      self.swap(index, largest)
    self.max_heapify(largest)

  def is_leaf(self, index):
    # Leaves have index between i and size - 1
    i = self.size // 2
    return index >= i and index <= self.size - 1

  def swap(self, a, b):
    temp = self.arr[a]
    self.arr[a] = self.arr[b]
    self.arr[b] = temp

  def print_heap(self):
    if self.size == 0:
      print('Underflow')
      return
    print('Current heap is:')
    for i in range(self.size):
      print(self.arr[i], end=' ')
    print()

def print_instructions():
  print('---Commands List---')
  print('1 -> Insert Element')
  print('2 -> Build Heap')
  print('3 -> Print Heap')
  print('4 -> Exit')

  
if __name__ == '__main__':
  max_size = int(input('Enter max size of heap: '))
  heap = MaxHeap(max_size)
  while True:
    choice = int(input('[Press 0 for commands list] Enter command: '))
    if choice == 0:
      print_instructions()
    elif choice == 1:
      value = int(input('Enter element: '))
      heap.insert(value)
    elif choice == 2:
      heap.build_heap()
      print('Heap built')
    elif choice == 3:
      heap.print_heap()
    elif choice == 4:
      print('Exited')
      break
    else:
      print('Invalid Choice!')

