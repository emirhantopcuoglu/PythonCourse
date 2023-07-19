import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        self.loadUser()

    def loadUser(self):
        if(os.path.exists("users.json")):
            with open("users.json","r") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    print(user)
    def register(self,user : User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")
        
    def login(self):
        pass
    def savetoFile(self):
        list = []
        for users in self.users:
            list.append(json.dumps(user,__dict__))

        with open("users.json","w") as file:
            json.dump(list,file)
repository = UserRepository()

while True:
    print('Menü'.center(50,'*'))
    secim = input('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeciminiz: ')
    if(secim == '5'):
        break
    else:
        if(secim == '1'):
            # register
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            
            user = User(username=username,password=password,email=email)
            repository.register(user)
        elif(secim == '2'):
            # login
            pass
        elif(secim == '3'):
            # logout
            pass
        elif(secim == '4'):
            # identity
            pass
        else:
            print("Hatalı giriş!")