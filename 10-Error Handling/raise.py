# x = 10
# if x > 5:
#     raise Exception("x 5 den büyük olamaz")


# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 8 karakterden oluşmalı")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içermeli")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola büyük harf içermeli")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola rakam içermeli")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Parola alpha numeric karakter içermeli")
#     elif re.search("\s",psw):
#         raise Exception("Parola boşluk içermemeli")
#     else:
#         print('Geçerli parola')
# password = '12345678aA$'
# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print('Geçerli parola: else')
# finally:
#     print('Validation tamamlandı')

class Person():
    def __init__(self,name,year):
        if len(name) > 10 :
            raise Exception("Name 10 karakterden fazla olamaz")
        else:
            self.name = name
p = Person('Aaaaaaaaa',1990)