import datetime 

def convert_date_string(date_string):
   return datetime.datetime.strptime(date_string, "%d-%m-%y")