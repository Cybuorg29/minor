class Node: 
    def __init__(self,data): 
        self.data = data
        self.next = None
  
class LinkedList: 
    def __init__(self):  
        self.head = None
  
    def assignValues(self, dataList): 
        node1 = Node(dataList[0]) 
        node2 = Node(dataList[1]) 
        node3 = Node(dataList[2]) 
        node4 = Node(dataList[3]) 
  
        self.head = node1 
        node1.next = node2 
        node2.next = node3 
        node3.next = node4 

dataList = [1, 2, 3, 4] 
llist = LinkedList() 
llist.assignValues(dataList)