def product_of_all_except_self(lst):
    """This function takes an array of integers and returns an array where each index is the product of all the numbers except for the number at that index."""
    products = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= lst[j]
        products.append(product)
    return products