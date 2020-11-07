from Node import Node

class Codec:
    def __init__(self):
        self.EMPTY = ','
        self.str = []
        self.index = 0
        
    def serialHelper(self, root):
        if not root:
            self.str.append(self.EMPTY)
            return None
        self.str.append(root.val)
        self.serialHelper(root.left)
        self.serialHelper(root.right)
    
    def serialize(self, root):
        self.str = []
        self.serialHelper(root)
        return '.'.join([str(s) for s in self.str])
    
    def deserialHelper(self):
        if self.index == len(self.str):
            return None
        val = self.str[self.index]
        self.index += 1
        if val == self.EMPTY:
            return None
        root = Node(val)
        root.left = self.deserialHelper()
        root.right = self.deserialHelper()
        return root
        
    def deserialize(self, data):
        self.index = 0
        self.str = data.split('.')
        return self.deserialHelper()