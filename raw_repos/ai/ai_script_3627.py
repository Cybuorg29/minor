def findMax(root): 
    if root == None: # if tree is empty
        return -1
    while root.right: # Move right in  BST till the last node
        root = root.right
    return root.key