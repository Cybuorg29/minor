class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def maxDepth(node):
    if node is None:
        return 0
    else:
        leftDepth = maxDepth(node.left)
        rightDepth = maxDepth(node.right)

        if leftDepth > rightDepth: 
            return leftDepth+1
        else: 
            return rightDepth+1