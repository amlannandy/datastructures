class HashTable:
  def __init__(self, b):
    self.bucket = b
    self.table = []
    for i in range(b):
      self.table.append(list())
    
  def insert(self, key):
    i = key % self.bucket
    self.table[i].append(key)

  def delete(self, key):
    i = key % self.bucket
    self.table[i].remove(key)

  def search(self, key):
    i = key % self.bucket
    for k in self.bucket[i]:
      if k == key:
        return True
    return False
