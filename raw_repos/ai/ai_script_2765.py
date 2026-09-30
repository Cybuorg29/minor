import threading

class ThreadSafeQueue():
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def push(self, item):
        with self.lock:
            self.queue.append(item)

    def pop(self):
        with self.lock:
            item = self.queue.pop(0)
        return item