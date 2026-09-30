def search_BST(root, key): 
  
    # Base Condition 
    if root is None or root.val == key: 
        return root 
  
    # If key is greater than root's key 
    if root.val < key: 
        return search_BST(root.right, key) 
  
    # If key is smaller than root's key 
    return search_BST(root.left, key) 
  
# Driver Code 
root = Node(5)
root.left = Node(3) 
root.right = Node(8)
root.left.left = Node(2) 
root.left.right = Node(4) 
root.right.left = Node(6) 
root.right.right = Node(9) 
  
key = 3
node = search_BST(root, key) 
if node:
    print("Found") 
else: 
    print("Not Found")