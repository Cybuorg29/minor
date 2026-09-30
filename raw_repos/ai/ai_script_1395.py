class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None: 
            curr_node = curr_node.next
        curr_node.next = new_node

    def delete_by_value(self, data):
        if self.head is None:
            return
        curr_node = self.head
        if curr_node.data == data:
            self.head = curr_node.next
            return
        prev_node = curr_node
        while curr_node is not None:
            if curr_node.data == data:
                break
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next