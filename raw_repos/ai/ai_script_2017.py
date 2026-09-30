import java.util.HashMap;
 
public class LRUCache { 
  
    // Custom Doubly Linked List 
    static class CacheNode { 
        CacheNode prev; 
        CacheNode next; 
        int key; 
        int value; 
    } 
  
    // Map containing the Keys 
    private HashMap<Integer, CacheNode> map 
        = new HashMap<Integer, CacheNode>(); 
  
    // Maximum number of elements in the cache 
    private int capacity; 
  
    // Current size 
    private int size; 
  
    // Head of the DLL 
    private CacheNode head; 
  
    // Tail of the DLL 
    private CacheNode tail; 
  
    public LRUCache(int capacity) { 
        this.capacity = capacity; 
        this.size = 0; 
    } 
  
    // Lookup a key in the cache 
    public int get(int key) { 
  
        // Return -1 if no such key exists 
        if (!map.containsKey(key)) { 
            return -1; 
        } 
  
        // Get the node 
        CacheNode node = map.get(key); 
  
        // Delete the node 
        removeNode(node); 
  
        // Put it at the head 
        addAtHead(node); 
  
        // Return its value 
        return node.value; 
    } 
  
    // Add a new node to the cache 
    public void put(int key, int value) { 
        CacheNode node = new CacheNode(); 
        node.key = key; 
        node.value = value; 
  
        // Check if the node is already present 
        if (map.containsKey(key)) { 
            CacheNode oldNode = map.get(key); 
            removeNode(oldNode); 
            addAtHead(node); 
            map.put(key, node); 
        } else { 
            // Add at the front of the list 
            if (size == capacity) { 
                // Delete the last node 
                map.remove(tail.key); 
                removeNode(tail); 
            } 
            addAtHead(node); 
            map.put(key, node); 
        } 
    } 
  
    // Remove a node from the list 
    public void removeNode(CacheNode node) { 
        if (node.prev != null) { 
            node.prev.next = node.next; 
        } else { 
            head = node.next; 
        } 
  
        if (node.next != null) { 
            node.next.prev = node.prev; 
        } else { 
            tail = node.prev; 
        } 
  
        size--; 
    } 
  
    // Put a node at the front of the list 
    public void addAtHead(CacheNode node) { 
        node.next = null; 
        node.prev = null; 
  
        if (head == null) { 
            head = node; 
            tail = node; 
        } else { 
            node.next = head; 
            head.prev = node; 
            head = node; 
        } 
  
        size++; 
    } 
}