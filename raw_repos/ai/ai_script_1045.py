def third_largest(root):
    if root is None:
        return None
 
    queue = []
    queue.append(root)
    while len(queue):
        curr = queue.pop(0)
 
        if curr.right:
            queue.append(curr.right)
        if curr.left:
            queue.append(curr.left)
 
    if len(queue)>1:
        return queue[1].val
    else:
        return root.val