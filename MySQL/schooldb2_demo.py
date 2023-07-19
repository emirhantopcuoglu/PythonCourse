import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "schooldb"
)

mycursor = mydb.cursor()
sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s)"
ogrenciler = [
    ("101","Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E"),
    ("102","Canan","Tan",datetime.datetime(2005,7,7),"K"),
    ("103","Ali","Cenk",datetime.datetime(2003,8,12),"E")
]
mycursor.executemany(sql,ogrenciler)

try:
    mydb.commit() # bağlantı sağlanır
    print(f'{mycursor.rowcount} tane kayıt eklendi.')
except mysql.connector.Error as err:
    print('Hata: ',err)
finally:
    mydb.close()
