# Girilen sayı asal mı değil mi?
sayi = int(input('Sayı girin: '))
if sayi%2 != 0 and sayi%3 != 0 and sayi%5 != 0 and sayi%7 != 0:
    print(f"{sayi} asal bir sayıdır.") 
else:
    print(f"{sayi} asal bir sayı değildir." )