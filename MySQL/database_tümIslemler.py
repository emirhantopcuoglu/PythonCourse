import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "deneme"
)

cursor = dataBase.cursor()
# cursor.execute("CREATE DATABASE deneme")  <-- [DATABASE OLUŞTURMA]

# TABLO OLUŞTURMA: 
# products = "CREATE TABLE Product(Name VARCHAR(40),Price DOUBLE,Year INT)"
# cursor.execute(products)                                                      
# dataBase.close()

# TEK TEK ELEMAN EKLEME:
# sql = "INSERT INTO Product(Name,Price,Year) VALUES(%s,%s,%s)"
# values = ("IPhone 11",15000,2021)
# cursor.execute(sql,values)
# dataBase.commit()                                                    
# print(f"{cursor.rowcount} adet ürün eklendi.")
# dataBase.close()

# BİRDEN FAZLA ELEMAN EKLEME:
# sql = "INSERT INTO Product(Name,Price,Year) VALUES(%s,%s,%s)"
# values = [("Kalem",10,2022),("Mouse",200,2022),("Kitap",25.50,1998)]
# cursor.executemany(sql,values)
# dataBase.commit()                                                 
# print(cursor.rowcount," adet ürün eklendi.")
# dataBase.close()

# SELECT İŞLEMİ:
# sql = "Select * From product"
# cursor.execute(sql)           
# result = cursor.fetchall()
# for i in result:
#     print(i)

# BELLİ SÜTUNLARI SELECT İŞLEMİ:
# sql = "SELECT Name,Price FROM product"
# cursor.execute(sql)           
# result = cursor.fetchall()
# for i in result:
#     print(i)

# WHERE İŞLEMİ(belli bir eleman bulma,listeleme):
# sql = "SELECT * FROM product WHERE Price < 1000"
# cursor.execute(sql)                               
# result = cursor.fetchall()
# for i in result:
#     print(i)

# ORDER BY İŞLEMİ(elemanları sıralama):
# sql = "SELECT * FROM product ORDER BY Price"      <-- küçükten büyüğe sıralama
# sql = "SELECT * FROM product ORDER BY Price DESC" <-- büyükten küçüğe sıralama (DESC)
# cursor.execute(sql)                                   
# result = cursor.fetchall()
# for i in result:
#     print(i)

# KAYIT SİLME İŞLEMİ:
# sql = "DELETE FROM product WHERE name='Kalem'"
# cursor.execute(sql)
# try:
#     dataBase.commit()
#     print(f'{cursor.rowcount} adet kayıt silindi.')  
# except mysql.connector.Error as err:
#     print("Hata: ",err)
# finally:
#     dataBase.close()
#     print("Database kapatıldı.")

# UPDATE İŞLEMİ: 
# sql = "UPDATE product SET Name='Kulaklık',Price='700',Year='2020' WHERE Name='Kitap'"
# cursor.execute(sql)
# try:
#     dataBase.commit()
#     print(f'{cursor.rowcount} adet kayıt güncellendi.')  
# except mysql.connector.Error as err:
#     print("Hata: ",err)
# finally:
#     dataBase.close()
#     print("Database kapatıldı.")

# JOIN İŞLEMİ:
# sql = "SELECT * FROM products inner join Categories on Categories.id=products.Categoryid"
# sql = "SELECT * FROM products inner join Categories on Categories.id=products.Categoryid WHERE Categories.name='Telefon'"
