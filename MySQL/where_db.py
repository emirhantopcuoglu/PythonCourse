import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "node-app"
)
cursor = connection.cursor()

# cursor.execute("SELECT * FROM products where id=2 ")
# cursor.execute("SELECT * FROM products where description LIKE '%telefon%'") 

# cursor.execute("SELECT * FROM products Order By price") # alfabetik veya artan sıralama
# cursor.execute("SELECT * FROM products Order By price DESC") # azalan sıralama

result = cursor.fetchall()
print(result)