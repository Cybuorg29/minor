class Zoo:
    def __init__(self):
        self.records = {}

    def add_record(self, animal, count):
        if animal in self.records:
            self.records[animal] += count
        else:
            self.records[animal] = count

    def get_count(self, animal):
        if animal in self.records:
            return self.records[animal]
        else:
            return 0