from itertools import count


name = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

# 'Cenk' ismini listenin sonuna ekleyin.
name.append('Cenk')

# 'Sena' ismini listenin başına ekleyin.
name.insert(0,'Sena')

# 'Deniz' isminin indeksi kaçtır?

print(name.index('Deniz'))

# 'Deniz' ismini listeden silin.
name.remove('Deniz')
print(name)

# 'Ali' listenin elemanı mıdır?
print('Ali' in name)

# Liste elemanlarını ters çevirin.
name.reverse()
print(name)

# Liste elemanlarını alfabetik olarak sıralayın.
name.sort()
print(name)

# years listesini küçükten büyüğe sıralayın.
years.sort()
print(years)

# str = 'Chavrolet,Dacia' stringini listeye çevirin
str = 'Chavrolet,Dacia'
str = str.split()
print(str)

# years listesinin en büyük ve en küçük elemanı?
print(min(years))
print(max(years))

# years listesinde kaç tane 1998 vardır?
print(years.count(1998))

# years listesinin tüm elemanlarını silin.
years.clear()
print(years)

# Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayın.
markalar = []
marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)


