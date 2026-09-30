class WordDictionary(object): 
    def __init__(self): 
        self.words = {} 

    def add_definition(self, word, definition): 
        self.words[word] = definition

    def lookup_definition(self, word): 
        if word in self.words: 
            return self.words[word]
        else: 
            return None

    def delete_word(self, word): 
        del self.words[word]