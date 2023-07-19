# Dosya açmak ve oluşturmak için 'open()' fonksiyonu kullanılır.
# Kullanımı : open(dosya_adi,dosya_erisme_modu)
# dosya_erisme_modu --> dosyayı hangi amaçla açtığımızı belirtir

# "w" : (Write) yazma modu. Dosyayı konumda oluşturur.
# *** Dosya içeriğini siler ve yeniden ekleme yapar.
# file = open("newfile.txt","w")
# file = open("C:/Users/emirh/python/Files/newfile.txt","w")
# file.close()
# file = open("newfile.txt","w")
# file.write("Python")
# file.close()

# "a" : (Append) ekleme. Dosyayı konumda yoksa oluşturur.
# file = open("newfile.txt","a")
# file.write("Python Programming")
# file.close()

# "x" : (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("newfile2.txt","x")

# "r" : (Read) okuma.varsayılan. Dosya konumda yoksa hata verir.
