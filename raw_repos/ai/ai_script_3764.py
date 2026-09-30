class Stack:

    class Node:
        def __init__(self, value):#, next=None):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    def push(self, value):
        node = self.Node(value)
        node.next = self.head
        self.head = node
        self.count += 1

    def pop(self):
        if self.head == None:
            return None
        result = self.head.value
        self.head = self.head.next
        self.count -= 1
        return result