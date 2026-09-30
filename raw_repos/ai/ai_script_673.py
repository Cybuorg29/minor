def format_date(date, date_format):
 date = date.split('-') 
 day = date[2]
 month = date[1]
 year = date[0]
 if date_format == "dd/mm/yyyy": 
  formatted_date = day + "/" + month + "/" + year
 return formatted_date