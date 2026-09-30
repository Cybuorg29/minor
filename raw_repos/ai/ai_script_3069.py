import MySQLdb


query = "SELECT * FROM users WHERE username = %s"
db = MySQLdb.connect(host="localhost", user="user", passwd="pass", db="mydb")
cur = db.cursor()
cur.execute(query, (username,))