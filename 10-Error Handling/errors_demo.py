liste = ["1","2","5a","10b","abc"]

# 1) Listenin elemanları içindeki sayısal değerleri bulun.
"""for i in liste:
    try:
        result = int(i)
        print(result)
    except ValueError :
        continue   """
# 2) Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde
# hata mesajı yazın.
"""while True:
    sayi = input('sayı girin: ')
    if sayi == 'q':
        break
    try:
        result = float(sayi)
    except ValueError:
        print('Hata')
    else:
        print('sayi girdiniz.') """
# 3) Girilen parola içinde Türkçe karakter varsa hata verin.
"""tr = 'şöçğıİĞÜÇŞI'
psw = input('parola: ')
for i in psw:
    if i in tr:
        raise TypeError('Parola türkçe karakter içeremez.')
    else: 
        pass

print('Geçerli parola') """

# 4) Faktöriyel fonk. oluşturup fonksiyona gelen değer için hata mesajı verin

def fact(x):
    x = int(x)
    if x < 0 :
        raise ValueError('Lütfen 0 veya daha büyük bir değer girin')
    else:
        f = 1
        for i in range(1,x+1):
            f *= i
        
        return f

x = input('x: ')
try: 
    print(fact(x))
except Exception as e:
    print('Hata: ',e)
    



        