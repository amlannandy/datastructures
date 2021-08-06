from max_heap import MaxHeap

class MaxHeapWithIncreaseKey(MaxHeap):
  def __init__(self, max_size):
    super().__init__(max_size)

  def increase_key(self, i, val):
    if i >= self.size:
      print('Invalid key')
      return
    if val <= self.arr[i]:
      print('Invalid Value')
      return
    self.arr[i] = val
    while i > 0 and self.arr[i] > self.arr[(i-1)//2]:
      self.swap(i, (i-1)//2)
      i = i//2

def print_instructions():
  print('---Commands List---')
  print('1 -> Insert Element')
  print('2 -> Build Heap')
  print('3 -> Print Heap')
  print('4 -> Increase Key')
  print('5 -> Exit')

  

max_size = int(input('Enter max size of heap: '))
heap = MaxHeapWithIncreaseKey(max_size)
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
    i = int(input('Enter index of key: '))
    val = int(input('Enter new value of key: '))
    heap.increase_key(i, val)
    print('Key increased')
  elif choice == 5:
    print('Exited')
    break
  else:
    print('Invalid Choice!')    