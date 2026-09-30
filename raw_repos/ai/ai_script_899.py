def tree_depth(root): 
    if root is None: 
        return 0 ;  
  
    else :  
        left_height = tree_depth(root.left) 
        right_height = tree_depth(root.right) 
  
        if (left_height > right_height): 
            return left_height+1
        else: 
            return right_height+1