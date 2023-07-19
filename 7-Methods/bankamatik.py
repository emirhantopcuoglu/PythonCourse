hesapA = {
    'ad' : 'Ali X',
    'hesapNo' : '123',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

hesapB = {
    'ad' : 'Can Y',
    'hesapNo' : '456',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye'] >= miktar:
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı?(e/h)')
            if ekHesapKullanimi == 'e':
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} numaralı hesabınızda {hesap['bakiye']} bulunmaktadır.")

def bakiyeSorgulama(hesap):
    print(f"{hesap['hesapNo']} no'lu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")

#paraCek(hesapA,5000)
bakiyeSorgulama(hesapB)
