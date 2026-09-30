class Node {
  int data;
  Node next;
  Node(int data) { 
    this.data = data; 
    next = null;
  }
}

class LinkedList {
  Node head;
  public void insertNode(int data) { 
    Node new_node = new Node(data); 
    if (head == null) { 
        head = new_node;
        return;
    }
    Node last = head;  
    while (last.next != null) {
        last = last.next;
    }
    last.next = new_node; 
  } 
}

LinkedList list = new LinkedList();
list.insertNode(2);
list.insertNode(6);
list.insertNode(7);
list.insertNode(8);
list.insertNode(10);