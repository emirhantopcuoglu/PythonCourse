# with open("newfile.txt","r+") as file:
#     file.seek(20)
#     file.write("Deneme")

# with open("newfile.txt","r+") as file: # r+ hem okuma hem de yazma modunu temsil ediyor.
#     print(file.read())

# Sayfa sonunda güncelleme: 
# with open("newfile.txt","a") as file:
#     file.write("Yeni Deneme")
# with open("newfile.txt","r") as file:
#     print(file.read())

# Sayfa başında güncelleme: 
# with open("newfile.txt","r+") as file:
#     content = file.read()
#     content = "Computer" + content
#     print(content)

# Sayfa ortasında güncelleme:
# with open("newfile.txt","r+") as file:
#     list = file.readlines()
#     list.insert(1,"Software\n")
#     file.seek(0)
#     # for i in list:
#     #     print(i)
#     # print(list)
#     file.writelines(list)

# with open("newfile.txt","r") as file:
#     print(file.read())