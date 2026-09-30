def count_values_greater_than_root(root):
    count = 0
    if root.right:
        count += 1 + count_values_greater_than_root(root.right)
    if root.left:
        count += count_values_greater_than_root(root.left)
    return count