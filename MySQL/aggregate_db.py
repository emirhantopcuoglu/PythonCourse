import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "node-app"
)
cursor = connection.cursor()
# sql = "SELECT COUNT(*) FROM products" # Toplam kayıt sayısı
# sql = "SELECT AVG(price) FROM products" # Ortalama
# sql = "SELECT SUM(price) FROM products" # Toplama 
# sql = "SELECT MIN(price) FROM products" # Minimum değer
# sql = "SELECT MAX(price) FROM products" # Maximum değer
sql = "SELECT name FROM products Where price = (SELECT MAX(price) FROM products) " # Max değere sahip kaydın ismi
cursor.execute(sql)
result = cursor.fetchone()
print(f'result: {result[0]}')
