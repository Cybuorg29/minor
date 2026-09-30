# Node class 
class Node: 
 
	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 

# Linked List class 
class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new node at the beginning 
	def insert_at_head(self, new_data): 
		
		# Create a new node 
		new_node = Node(new_data) 

		# update the new nodes next to old head
		new_node.next = self.head 

		# update head to new node 
		self.head = new_node