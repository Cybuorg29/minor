class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        hash_value = hash(key)
        index = hash_value%self.size
        if self.table[index] == None:
            self.table[index] = [key, value]
        else:
            self.table[index].append([key,value])

    # Other methods go here

# Create a hashtable
ht = HashTable(8)

# Insert elements
ht.insert('apple', 5)
ht.insert('banana', 8)
ht.insert('strawberry', 11)
ht.insert('kiwi', 2)
ht.insert('mango', 6)