# try:
#     file = open("newfile.txt") # "r" belirtilmese bile default olarak read modu kullanılır.
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     file.close()
"""###############################################"""
file = open("newfile.txt","r")

# for döngüsü ile okuma:
# for i in file:
#     print(i,end="") # end="" satır sonrası boşluk bırakılmasını engeller.
"""###############################################"""
# read() fonksiyonu ile okuma:
# content1 = file.read()
# print("İçerik 1:")
# print(content1)

# content2 = file.read()
# print("İçerik 2:")
# print(content2)   # içerik 2'den sonra bir şey okunmaz çünkü dosya kapatılmadı.

# content = file.read(5) # 5 karakter okur
# content = file.read(3) # kaldığı yerden 3 karakter daha okur
# print(content)
"""###############################################"""
# readline() fonksiyonu ile okuma:
# print(file.readline(),end="") # sadece 1 satır okur.
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
"""###############################################"""
# readlines() fonksiyonu ile okuma: 
# print(file.readlines()) # her satırı listeye eleman olarak ekler
file.close()