"""
Construct a Fibonacci Heap class
"""

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.nodes = []
    
    def insert(self, node):
        self.nodes.append(node)
        if self.min is None or node.key < self.min.key:
            self.min = node
    
    def extract_min(self):
        min_node = self.min
        self.min = None
        return min_node 

if __name__ == '__main__':
    heap = FibonacciHeap()
    node1 = Node(3)
    node2 = Node(10)
    heap.insert(node1)
    heap.insert(node2)
    print(heap.extract_min().data) # prints 3