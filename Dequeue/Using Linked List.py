class Node:
  def __init__(self, val):
    self.val = val
    self.prev = None
    self.next = None

class Dequeue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueueFront(self, val):
    node = Node(val)
    if not self.front:
      self.front = node
      self.rear = node
    

  def isEmpty(self):
    if not self.front and not self.rear:
      return True
    return False