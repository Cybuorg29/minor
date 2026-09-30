def traverse_preorder(root):
    if (root == None):
        return
    else:
        print(root.val)
        traverse_preorder(root.left)
        traverse_preorder(root.right)