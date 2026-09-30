def calculate_total_amount(products, prices):
 total_amount = 0 
 for i in range(len(products)):
 total_amount = total_amount + (products[i] * prices[i])
 return total_amount