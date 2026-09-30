class DoublyLinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None

    def append(self, val): 
        current = self 
        while current.next is not None: 
            current = current.next
        current.next = DoublyLinkedList(val) 
        current.next.previous = current