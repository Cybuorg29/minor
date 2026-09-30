class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

def printList(head): 
    temp = head 
    while(temp): 
        print (temp.data, end=" ") 
        temp = temp.next