def extractDigits(num):
    extracted_list = []
    while num > 0:
        extracted_list.append(num%10)
        num //= 10
    extracted_list.sort(reverse=True)
    return extracted_list