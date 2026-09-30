public class LinkedList {
 
    Node head;
 
    static class Node {
        int data;
        Node next;
 
        Node(int d) {
            data = d;
            next = null;
        }
    }
 
    public void deleteNode(int position) {
        if (head == null) {
            return;
        }
        Node temp = head;

        if(position == 0){
            head = temp.next;
            return;
        }

        for (int i = 0; temp != null && i < position - 1; i++) {
            temp = temp.next;
        }

        if (temp == null || temp.next == null) {
            return;
        }

        // Unlink the deleted node from the linked list
        Node next = temp.next.next;
        temp.next = next; 
    }

}