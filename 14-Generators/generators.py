# Generator, bellekte yer tutmayan iterator üretir.
# def cube():
#     result = []

#     for i in range(5): --> Bu liste bellek üzerinde yer tutar.5 eleman için çok sorun değil lakin
#         result.append(i**3) --> çok daha fazla eleman olursa (örn. 5000) bellekte çok daha fazla yer tutacaktır. 
#     return result

# print(cube())
"""************************"""
def cube():
    for i in range(5):
        yield i ** 3   # Üretilir ve hemen kullanılır. Bellekte yer tutmaz.

# generator = cube()      --> Şeklinde 
# iterator = iter(generator) --> kullanılabilir.

iterator = cube()  

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for i in iterator:
    print(i)

# veya daha kısaca:

# for i in cube():  --> Şeklinde
#   print(i)          -->  kullanılabilir.
"""************************"""
generator = (i for i in range(5)) # --> Generator objesi oluşturur.
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
for i in generator:
    print(i)

