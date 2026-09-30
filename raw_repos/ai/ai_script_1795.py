class Stream:
    def __init__(self):
        self.stream = [None, None, None, None, None]

    # This function adds a number to the start (index 0) of the stream and then shifts the other elements to the right
    def add(self, num):
        for i in reversed(range(1, len(self.stream))):
            self.stream[i] = self.stream[i-1]

        self.stream[0] = num

    # This function returns a list of the current elements from the stream
    def list(self):
        return self.stream