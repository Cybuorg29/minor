def age_calc(date_of_birth):
    """
    This function takes in a date of birth and calculates 
    the age in years and months.
    """
    today = datetime.date.today()
    age_years = today.year - date_of_birth.year
    age_months = today.month - date_of_birth.month
    if age_months < 0:
        age_years -= 1
        age_months += 12
    return age_years, age_months

date_of_birth = datetime.date(1998, 6, 4)
print(age_calc(date_of_birth))

# Output: (21, 10)