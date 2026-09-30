class Node { 
    int data; 
    Node previous; 
    Node next;  
    public Node(int data) { 
        this.data = data; 
        this.previous = null; 
        this.next = null; 
    } 
} 
  
class DoublyLinkedList { 
    Node head; 
  
    // Inserts a new Node at front of the list 
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
  
        new_node.next = head; 
        new_node.previous = null; 
  
        if (head != null) 
            head.previous = new_node; 
  
        head = new_node; 
    } 
  
    // Delete a node from the list 
    void deleteNode(Node node_ptr) 
    { 
        // If node to be deleted is head node 
        if (head == node_ptr) 
            head = node_ptr.next; 
  
        // Change next only if node to be deleted  
        // is NOT the last node 
        if (node_ptr.next != null) 
            node_ptr.next.previous = node_ptr.previous; 
  
        // Change prev only if node to be deleted  
        // is NOT the first node 
        if (node_ptr.previous != null) 
            node_ptr.previous.next = node_ptr.next; 
    } 
  
    // Display linked list 
    public void display() 
    { 
        Node last = null; 
        System.out.println("Doubly Linked List in forward \n"); 
        while (head != null) { 
            System.out.print(head.data + " <=> "); 
            last = head; 
            head = head.next; 
        } 
        System.out.println("null\n"); 
  
        System.out.println("Doubly Linked List in reverse \n"); 
        while (last != null) { 
            System.out.print(last.data + " <=> "); 
            last = last.previous; 
        } 
        System.out.println("null\n"); 
    } 
}