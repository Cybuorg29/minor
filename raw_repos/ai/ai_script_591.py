# Function to delete all the elements 
# of the linked list 
def deleteList(head_node): 
    # Store head node 
    curr = head_node 
    prev = None

    # Traverse the list and delete 
    # each node one by one 
    while(curr): 
        # Next node  
        next = curr.next
        # Free the current node 
        curr = None
        # Update prev and curr node 
        prev = curr 
        curr = next