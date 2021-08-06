from max_heap import MaxHeap

class MaxHeapWithSort(MaxHeap):
  def __init__(self, max_size):
    super().__init__(max_size)

  def sort(self):
    if self.size == 0:
      print('Underflow')
      return

    length = self.size

    self.build_heap()
    for i in reversed(range(1, self.size)):
      self.swap(0, i)
      self.size -= 1
      self.max_heapify(0)

    self.size = length

n = int(input('Enter size of array: '))
arr = list(map(int, input('Enter array elements: ').split()))

heap = MaxHeapWithSort(n)
for i in range(n):
  heap.insert(arr[i])

print('Current Array is:')
heap.print_heap()

heap.sort()

print('Sorted Array is:')
heap.print_heap()