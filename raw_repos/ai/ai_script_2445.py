class Node{
    int data; 
    Node next; 
        
    Node(int d){
        data = d; 
        next = null; 
    } 
} 

class LinkedList{ 
    Node head; 
        
    public void insert(int data){ 
        Node node = new Node(data); 
        if (head == null) { 
            head = node; 
        } 
        else { 
            Node n = head; 
            while (n.next != null) { 
                n = n.next; 
            } 
            n.next = node; 
        } 
    } 
}