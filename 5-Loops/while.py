x = 0
while x<=100:
    print(x)
    x+=1

a = 0
while a<=100:
    if(a % 2 == 1):
        print(f'{a} tek sayı')
        a += 1
    else:
        print(f'{a} çift sayı')
        a += 1

name = ''
while not name:
    name = str(input('İsminizi girin: '))
    
print(f"Merhaba {name}")
