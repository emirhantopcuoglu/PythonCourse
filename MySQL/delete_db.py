import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "node-app"
)
cursor = connection.cursor()
# sql = "DELETE FROM products" # Tüm kayıtlar silinir
# sql = "DELETE FROM products WHERE name LIKE '%S7%'" # adında S7 ifadesi geçen kayıt silinir
sql = "DELETE FROM products WHERE id=1"
cursor.execute(sql)
try:
    connection.commit()
    print(f'{cursor.rowcount} tane kayıt silindi')
except mysql.connector.Error as err:
    print("hata: ",err)
finally:
    connection.close()
    print("Database bağlantısı kapatıldı")