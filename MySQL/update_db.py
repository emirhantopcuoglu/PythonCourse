import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "node-app"
)
cursor = connection.cursor()
sql = "UPDATE products SET name='S22' WHERE id=5"
cursor.execute(sql)
try:
    connection.commit()
    print(f'{cursor.rowcount} tane kayıt güncellendi')
except mysql.connector.Error as err:
    print("hata: ",err)
finally:
    connection.close()
    print("Database bağlantısı kapatıldı")
