import os
# print(os.name) # işletim sistemi adı
# print(os.getcwd()) # dosya yolu

# os.mkdir("newdirectory") # yeni klasör oluşturur
# os.chdir("C:\\") dosya dizinini değiştirir
# os.chdir('../..') 2 üst klasöre geçer
# os.makedirs("newdirectory/yeniklasör") # klasör içine klasör oluşturma

# print(os.listdir()) # etkin olan dizin içerisindeki klasörleri gösterir

# for dosya in os.listdir(): # '.py' uzantılı dosyaları yazdıran döngü
    #if dosya.endswith(".py"):
        #print(dosya)

# os.system('notepad.exe') # bilgisayardaki bir uygulamayı çalıştırma
# os.rename('newdirectory','yeniklasör') # klasör adı değiştirme
# os.rmdir('yeniklasör') # klasör silme
# os.removedirs('yeniklasör/yeniklasör') # klasör silme (alt dizindeki)
"""********************"""
# path:
result = os.path.abspath("newfile.txt") # dosyanın tam konumunu yazdırır
result = os.path.dirname('C:/Users/emirh/python/newfile.txt') # tam konumu yazılan dosyanın dizin ismi
result = os.path.dirname(os.path.abspath("newfile.txt")) # dosyanın konumunu bilmiyorsak bu şekilde öğrenebiliriz
result = os.path.exists('newfile.txt') # dosya varsa True yoksa False döndürür
result = os.path.isdir('C:/Users/emirh/python/newfile.txt') # ilgili dosya klasörse True değilse False döndürür
result = os.path.isfile('C:/Users/emirh/python/newfile.txt') # dosya mı dizi mi
result = os.path.join("D:\\","deneme","deneme1")
result = os.path.split("D:\\deneme")
result = os.path.splitext("newfile.txt") # dosyanın ismiyle uzantısını ayırır
print(result[0])
print(result[1])
print(result)

