class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def Insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.Insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.Insert(data)
        else:
            self.data = data