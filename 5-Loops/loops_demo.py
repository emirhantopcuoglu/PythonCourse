import random
sayi = random.randint(1,100)
hak = 5

while hak > 0:
    hak -= 1
    tahmin = int(input("Tahmin giriniz: "))
    if tahmin == sayi:
        print("Tebrikler,bildiniz!")
        break
    elif tahmin > sayi:
        print("Azaltın")
    else :
        print("Yükseltin")
    if hak == 0:
        print(f"Oyun bitti. Cevap: {sayi} idi")