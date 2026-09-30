class Stack: 
  
    def __init__(self): 
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def is_empty(self):
        return self.stack == []
  
    def pop(self): 
        if self.is_empty():
            return None
          
        return self.stack.pop()