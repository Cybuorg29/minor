class PriorityQueue:
    def __init__(self):
        self.queue = []
 
    # Create the enqueue(data) method to add data inside the queue
    def enqueue(self, data):
        self.queue.append(data)
 
    # Create the dequeue() method to remove data from the queue
    def dequeue(self):
        if self.queue:
            min_item = min(self.queue)
            self.queue.remove(min_item)
            return min_item
        else:
            return None