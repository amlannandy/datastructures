from max_heap import MaxHeap

class MaxHeapWithDeleteMax(MaxHeap):
  def __init__(self, max_size):
    super().__init__(max_size)

  def delete_max(self):
    if self.size == 0:
      print('Underflow')
      return -1
    max_val = self.arr[0]
    self.arr[0] = self.arr[self.size - 1]
    self.size -= 1
    self.max_heapify(0)
    return max_val

def print_instructions():
  print('---Commands List---')
  print('1 -> Insert Element')
  print('2 -> Build Heap')
  print('3 -> Print Heap')
  print('4 -> Extract Max')
  print('5 -> Exit')

  

max_size = int(input('Enter max size of heap: '))
heap = MaxHeapWithDeleteMax(max_size)
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
    val = heap.delete_max()
    if val != -1:
      print('Extracted max is', val)
  elif choice == 5:
    print('Exited')
    break
  else:
    print('Invalid Choice!')    