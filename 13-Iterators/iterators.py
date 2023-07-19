liste = [1,2,3,4,5]
"""*********"""
# for i in liste: # liste iterable bir objedir. (iterable objeler "__iter__" metoduna sahiptir.)
#     print(i)
# print(dir(liste))
"""*********"""
iterator = iter(liste)
# print(next(iterator)) # iterator'ü next() metoduyla her çağırdığımızda listenin bir elemanını ekrana yazdırır.
# print(next(iterator)) 
# print(next(iterator)) 
# print(next(iterator)) 
# print(next(iterator)) 

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration: # StopIteration hatası verdiğinde döngüden çıkar.
#         break
"""*********"""
class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else: 
            raise StopIteration
list = MyNumbers(10,20)
# for i in list:
#     print(i)
myiter = iter(list)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break