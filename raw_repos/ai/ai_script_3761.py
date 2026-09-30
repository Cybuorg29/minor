class BinarySearchTree:
 
    def __init__(self, value): 
        self.left = None
        self.right = None
        self.value = value
 
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
 
    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)