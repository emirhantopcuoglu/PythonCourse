import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "node-app"
)
cursor = connection.cursor()

# cursor.execute("Select * From products") # "*",bütün kolonları seçtiğimiz anlamına geliyor.
cursor.execute("Select name,price From products")

# result = cursor.fetchall() # fetchall() fonksiyonu, birden fazla kayıt almak için kullanılıyor.
# for i in result:
#     print(f"name: {i[0]}, price: {i[1]}")

result = cursor.fetchone() # fetchone() fonksiyonu, bulduğu ilk kaydı getirir. Yani tek bir kayıt getirmek için
# kullanılır.
print(f"name: {result[0]}, price: {result[1]}")
