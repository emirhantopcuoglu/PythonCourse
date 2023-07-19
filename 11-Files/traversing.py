with open("newfile.txt","r") as file: # with ile dosya okuduğumuzda işlem bitince dosya otomatik kapanır.
    content = file.read()
    print(content)
    file.seek(10) # imleci 10.konuma götürür.
    print(file.tell()) # tell() metodu, imlecin konumunu gösterir.

