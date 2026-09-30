def get_list_size(head):
    count = 0
    temp = head
    while(temp):
        count += 1
        temp = temp.next
    return count