def DFS(root):
    s = Stack()
    s.push(root)
    while (s.size() > 0):
        node = s.pop()
        # Do something with the node
        if (node.left != NULL):
            s.push(node.left)
        if (node.right != NULL):
            s.push(node.right)