def convert_to_minutes(time): 
    # Split the time into hours and minutes 
    h, m = map(int, time.split(':'))

    # Add 12 to the hours if the time is PM 
    if time.endswith('PM'): 
        h += 12
    return h * 60 + m

print(convert_to_minutes("12:30PM")) # 750