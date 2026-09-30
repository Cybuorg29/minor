# Validate if the inputs are valid dates
def validate_dates(date_list):
    if len(date_list) == 0:
        return True
    prev_date = date_list[0]
    for date in date_list[1:]:
        if date < prev_date:
            return False
        prev_date = date
    return True