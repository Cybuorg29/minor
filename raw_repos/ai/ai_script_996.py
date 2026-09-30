class ImmutableList:
    def __init__(self, list_values):
        self._dict = dict()
        for i, elem in enumerate(list_values):
            self._dict[i] = elem
    
    def __getitem__(self, item):
        return self._dict[item]
    
    def __len__(self):
        return len(self._dict)