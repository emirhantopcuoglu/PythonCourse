import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "mydatabase"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase") [database oluşturma]
# mycursor.execute("SHOW DATABASES") [databaseleri listeleme]
# for x in mycursor:   
#    print(x) 

# name ve adress adında 2 alana sahip,customers adında bir table oluşturma:
mycursor.execute("CREATE TABLE customers(name VARCHAR(255),adress VARCHAR(255))") 
