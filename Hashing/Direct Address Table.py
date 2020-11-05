class DirectAddressTable():
    
    def __init__(self, size):
        self.table = [False] * size
    
    def insert(self, item):
        self.table[item] = True

    def delete(self, item):
        self.table[item] = False

    def search(self, item):
        return self.table[item]

    def printInstructions(self):
        print('Commands List')
        print('1. Insert')
        print('2. Delete')
        print('3. Search')
        print('4. Exit')

table = DirectAddressTable(int(input('Enter table size: ')))
while True:
    choice = int(input('Enter your command [Press 0 for List]: '))
    if choice == 0:
        table.printInstructions()
    elif choice == 1:
        item = int(input('Enter item: '))
        table.insert(item)
    elif choice == 2:
        item = int(input('Enter item: '))
        table.delete(item)
    elif choice == 3:
        item = int(input('Enter item: '))
        print(table.search(item))
    else:
        break