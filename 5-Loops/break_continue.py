# name = 'Python'

# for letter in name:
#     if letter == 't':
#         break # -> döngü durur  
#     print(letter) 

# for letter in name:
#     if letter == 't':
#         continue # -> bulunduğu adımı iptal edip devam eder  
#     print(letter) 

# x = 0

# while x < 5:
#     if x == 2:
#         break # -> while döngüsünden çıkar
#     print(x)
#     x+=1

# while x < 5:
#     x+=1
#     if x == 2:
#         continue # -> bulunduğu adımı iptal edip devam eder
#     print(x)
#     x+=1

# 1'den 100'e kadar tek sayıların toplamı
x = 0
sum = 0
while x < 100:
    x += 1
    if x%2 == 0:
        continue
    sum += x
print(sum)
    


