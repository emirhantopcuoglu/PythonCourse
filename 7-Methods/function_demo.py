# Gönderilen bir kelimeyi ekranda istenilen kez yazan fonksiyon.
def printFunc(word,n):
    for i in range(n):
        print(word)
printFunc("Hello",5)

# Kendine gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonksiyon.
def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

result = listeyeCevir(1,2,3,'a','b')
print(result)

# Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon.
def asal(a,b):
    for sayi in range(a,b):
        if sayi%2!=0 and sayi%3!=0 and sayi%5!=0 and sayi%7!=0:
            print(sayi)
asal(10,20)

# Gönderilen bir sayının tam bölenlerini liste yapan fonksiyon.
def bolenler(sayi):
    bolenlerListesi = []
    for n in range(1,sayi):
        if sayi%n == 0:
            bolenlerListesi.append(n)
    return bolenlerListesi
bol = bolenler(30)
print(bol)
