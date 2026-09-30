def deleteNode(head, node): 
    if head == None: 
        return 
	  
    # If node to be deleted is head node 
    if head.val == node: 
        head = None
        return head 
	  
    # Find prev node 
    prev = None
    curr = head 
    while curr and curr.val != node: 
        prev = curr 
        curr = curr.next

    # Unlink node from linked list 
    prev.next = curr.next
    curr = None

    return head