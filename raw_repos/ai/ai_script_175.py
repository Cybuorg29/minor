# Define a StateMachine class
class StateMachine: 
    def __init__(self): 
        self.handlers = {} 
        self.startState = None
        self.endStates = [] 
  
    def add_state(self, state): 
        self.handlers[state.name] = state
  
    def set_start(self, name): 
        self.startState = name
  
    def set_end(self, name): 
        self.endStates.append(name) 
  
    def run(self): 
        try: 
            handler = self.handlers[self.startState] 
        except: 
            raise(Exception, "Must call .set_start() before .run()")
        while True:
            # Get the next keyboard event
            event = get_event()
            if event:
                newState = handler.run(event) 
            if newState.name in self.endStates: 
                break 
            else: 
                handler = self.handlers[newState.name]