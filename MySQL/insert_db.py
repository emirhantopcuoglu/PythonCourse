import mysql.connector

def InsertProduct(name,price,imageURL,description):
    connection = mysql.connector.connect(host = "localhost",user = "root", password = "1234", database = "node-app")
    cursor = connection.cursor()
    sql = "INSERT INTO Products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageURL,description)
    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'Son eklenen kaydın idsi: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("Hata: ",err)
    finally:
        connection.close()
        print("Database bağlantısı kapatıldı.")

name = input("Ürün adı: ")
price = input("Ürün fiyatı: ")
imageURL = input("URL: ")
description = input("Ürün açıklaması: ")

InsertProduct(name,price,imageURL,description)