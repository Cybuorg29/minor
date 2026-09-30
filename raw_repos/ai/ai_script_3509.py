def calculate_tax(price):
    tax_rate = 0.20
    total = price + (price * tax_rate)
    return round(total, 2)