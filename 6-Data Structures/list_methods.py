numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers) # minimum değeri verir
print(val)

val = max(numbers) # maksimum değeri verir
print(val)

val = min(letters) # alfabeye göre minimum değeri verir
print(val)

val = max(letters) # alfabeye göre maksimum değeri verir
print(val)

val = numbers[3:6]
print(val)

val = numbers[3:]
print(val)

val = numbers[:6]
print(val)

numbers[4] = 40
print(numbers)

numbers.append(49) # listeye yeni eleman ekleme
print(numbers)

numbers.insert(3,70) # 3.indekse 70 elemanını ekler
numbers.insert(-1,52) # sondan bir önceki indekse 52 elemanını ekler
print(numbers)

numbers.pop() # son elemanı siler
print(numbers)

numbers.pop(0) # 0 indeksli elemanı siler
print(numbers)

numbers.remove(52) # '52' elemanını siler
print(numbers)

numbers.sort() # büyükten küçüğe sıralar
letters.sort() # alfabetik olarak sıralar
print(numbers)
print(letters)

numbers.reverse() # listeyi tersine çevirir
print(numbers)

print(len(numbers)) # eleman sayısını verir
print(len(letters))

print(numbers.count(10)) # elemandan kaç tane bulunduğunu verir
print(letters.count('a'))

numbers.clear() # tüm elemanları siler
print(numbers)

