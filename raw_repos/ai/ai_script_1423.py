import mysql.connector

mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
)

cursor = mydb.cursor()

# execute SQL query to display all data in table
cursor.execute("SELECT * FROM myTable")

# print all of the table data
myresult = cursor.fetchall()

for row in myresult:
   print(row)