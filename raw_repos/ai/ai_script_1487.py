class SortedList:
    def __init__(self):
        self.items = []

    def add(self, item):
        i = 0
        while i < len(self.items) and self.items[i] < item:
            i += 1
        self.items.insert(i, item)

    def remove(self, item):
        i = 0
        while i < len(self.items) and self.items[i] != item:
            i += 1
        if i < len(self.items):
            del self.items[i]

    def remove_at(self, index):
        del self.items[index]