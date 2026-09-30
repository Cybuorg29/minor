class FrequencyTable:
    def __init__(self, arr):
        self.table = {}
        for num in arr:
            if num in self.table:
                self.table[num] += 1
            else:
                self.table[num] = 1
    def query(self, num):
        return self.table.get(num, 0)