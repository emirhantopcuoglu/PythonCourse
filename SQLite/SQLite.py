import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()
cursor.execute("SELECT * FROM customers ")
result = cursor.fetchall()
print(result)
connection.close()

# SQL komutları aynı şekilde kullanılır
