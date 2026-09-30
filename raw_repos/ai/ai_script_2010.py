def days_in_month(month):
 if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
  return 31
 elif month == 'February':
  return 28
 else:
  return 30
  
# Output
days_in_month('September') 
# Output 
30