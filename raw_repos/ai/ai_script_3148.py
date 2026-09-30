def extract_country_code(number):
    # Check if number is valid
    if len(number) == 13 and number[0] == '+':
        # Extract the country code
        cc = number[1:3]
        return cc

if __name__ == "__main__":
    number = "+91 983-741-3256"
    print(extract_country_code(number))