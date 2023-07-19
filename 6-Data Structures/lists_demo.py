# 'BMW,Mercedes,Opel,Mazda' elemanlarına sahip bir liste oluşturun.
liste = ['BMW','Mercedes','Opel','Mazda']
print(len(liste))
print(liste[0],liste[-1])

# Mazda ile Toyota'yı değiştirin.
liste[-1] = 'Toyota'
print(liste)

# 'Mercedes' listenin elemanı mıdır?
result = 'Mercedes' in liste 
print(result)

# Listenin son 2 elemanı yerine 'volkswagen' ve 'Renault' ekleyin
liste[-2:0] = ['Volkswagen','Renault']
print(liste)

# Audi ve Nissan ekleyin
liste = liste + ['Audi','Nissan']
print(liste)

# Listenin son elemanını silin
del liste[-1]
print(liste)

# Listeyi tersten yazdırın
print(liste[::-1])



