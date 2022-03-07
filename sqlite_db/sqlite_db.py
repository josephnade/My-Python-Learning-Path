import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

for i in result:
    print(i)

connection.close()