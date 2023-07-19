# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# def sayHello():
#     print("Hello")
# def sayGreeting():
#     print("greeting")
# sayHello = my_decorator(sayHello)
# sayHello()
"""++++++++"""
# @my_decorator
# def sayHello(name):
#     print("Hello",name)
# sayHello("world")
"""********************"""
import math
import time
def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+str(finish-start)+" saniye sürdü.")
def usAlma(a,b):
    print(math.pow(a,b))

def faktoriyel(num):
    print(math.factorial(num))

faktoriyel(5)

# Decoratorları kısaca şöyle düşünebiliriz: Bir metottaki işlemleri eğer birden fazla metotta kullanacaksak
# decoratorlardan faydalanabiliriz.