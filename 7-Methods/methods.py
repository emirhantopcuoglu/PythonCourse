# def methodAdı(): --> method oluşturma

def sayHello():
    print("Hello")
sayHello()

def sayHello(name = "World" ): # --> method parametresi girilmezse "World" yazar
    return "Hello " + name
msg1 = sayHello()    
msg2 = sayHello("python")
print(msg1)
print(msg2)

def total(num1,num2):
    return num1+num2
result = total(5,25)
print(result)

def yasHesapla(dogumYili):
    return 2022 - dogumYili 

def emekliligeKacYilKaldi(dogumYili):
    """
    DOCSTRING: Emekliliginize kac yil kaldigini hesaplar.
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    print(f"Emekliliğinize {emeklilik} yıl kaldı.")

emekliligeKacYilKaldi(2002)
print(help(emekliligeKacYilKaldi))