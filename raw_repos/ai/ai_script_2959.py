class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Given data
data = [5, 6, 2, 9, 0]

# Create linked list
linked_list = LinkedList()

for i in data:
    linked_list.insert(i)