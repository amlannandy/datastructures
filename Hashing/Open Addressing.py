class HashTable:
  def __init__(self, b):
    self.capacity = b
    self.table = [-1] * b
    self.size = 0

  def hash(self, key):
    return key % self.capacity
    
  def insert(self, key):
    if self.size == self.capacity:
      return False
    i = self.hash(key)
    while self.table[i] != [-1] and self.table[i] != [-2] and self.table[i] != key:
      i = (i + 1) % self.capacity
    if self.table[i] == key:
      return False
    self.table[i] = key
    self.size += 1
    return True

  def delete(self, key):
    if self.size == 0:
      return False
    i = self.hash(key)
    h = i
    while self.table[i] != -1:
      if self.table[i] == key:
        self.table[i] = -2
        self.capacity -= 1
        return True
      if i == h:
        return False
    return False

  def search(self, key):
    h = self.hash(key)
    i = h
    while self.table[i] != -1:
      if self.table[i] == key:
        return True
      i = (i + 1) % self.capacity
      if i == h:
        return False
    return False
