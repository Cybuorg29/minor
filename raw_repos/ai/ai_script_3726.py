def merge(head1, head2):
    # If either is empty
    if not head1 or not head2:
        return head1 or head2
    # if first linked list is smaller 
    if head1.data < head2.data:
        head1.next = merge(head1.next, head2)
        return head1
    else: # if second linked list is smaller or equal
        head2.next = merge(head1, head2.next)
        return head2