def maximum(head): 
    max = head.data 
    while head is not None: 
        if max < head.data: 
            max = head.data 
        head = head.next
    return max