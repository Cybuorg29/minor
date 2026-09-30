def print_leap_years(start_year, end_year): 
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(year)

print_leap_years(2015, 2050)