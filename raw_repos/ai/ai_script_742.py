def traverseTree(node):
    result = []
    if node is None:
        return []
    else:
        result.append(node.data)
        result += traverseTree(node.left)
        result += traverseTree(node.right)
    return result