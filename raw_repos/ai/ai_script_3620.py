def roman_numerals_sum(num1, num2):
    """This function takes two Roman numerals as parameters and outputs their sum in Roman numerals."""
    Int1 = int(roman.fromRoman(num1))
    Int2 = int(roman.fromRoman(num2))
    Sum = Int1 + Int2
    return roman.toRoman(Sum)