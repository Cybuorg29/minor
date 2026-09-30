import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table
c.execute('CREATE TABLE Course (course_name TEXT, course_id TEXT, course_description TEXT, course_instructor TEXT)')

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()