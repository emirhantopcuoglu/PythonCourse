import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "schooldb"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Student(Id INT,StudentNumber INT,Name VARCHAR(45),Surname VARCHAR(45),Birthdate INT,Gender VARCHAR(6))")

# database silme:
# mycursor.execute("DROP DATABASE schooldb")