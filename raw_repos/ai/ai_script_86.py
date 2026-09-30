// Java Program to convert binary tree to doubly linked list 
public class BinaryTreeToDLL { 
  
    Node root; 
      
    // A simple recursive function to convert a given Binary tree 
    // to Doubly Linked List 
    Node BTTDLL(Node root) { 
          
        // Base case 
        if (root == null) 
            return root; 
      
        // Convert the left subtree and link to root 
        if (root.left != null) { 
              
            // Convert the left subtree 
            Node left = BTTDLL(root.left); 
      
            // Find inorder predecessor. After this loop, left 
            // will point to the inorder predecessor 
            for (; left.right != null; left = left.right); 
      
            // Make root as next of the predecessor 
            left.right = root; 
      
            // Make predecssor as previous of root 
            root.left = left; 
        } 
      
        // Convert the right subtree and link to root 
        if (root.right != null) { 
              
            // Convert the right subtree 
            Node right = BTTDLL(root.right); 
      
            // Find inorder successor. After this loop, right 
            // will point to the inorder successor 
            for (; right.left != null; right = right.left); 
      
            // Make root as previous of successor 
            right.left = root; 
      
            // Make successor as next of root 
            root.right = right; 
        } 
      
        return root; 
    } 
}