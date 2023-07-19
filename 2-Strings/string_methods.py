message = " İstanbul büyük bir şehir."
message = message.upper() # Tüm harfleri büyük harfe çevirir.
print(message)

message = message.lower() # Tüm harfleri küçük harfe çevirir.
print(message)

message = message.title() # Her kelimenin baş harfini büyük harfe çevirir.
print(message)

message = message.capitalize() # İlk kelimenin baş harfini büyük harfe çevirir.
print(message)

message = message.strip() # Karakter dizisinin baş ve sondaki boşluk karakterlerini siler. 
print(message)

message = message.split() # Karakter dizisini parçalara ayırır.
print(message)
print(message[0])

message = ' '.join(message) # Birleştirmek için kullandık.
print(message) 

index = message.find("şehir") # Aradığımız kelimeyi bulmamızı sağlar.İlk karakterin kaçıncı indexte olduğunu gösterir.
print(index)

isFound = message.startswith('')
print(isFound)

isFound = message.endswith('.')
print(isFound)

message = message.replace('büyük','güzel') # büyük yerine güzel yazar.
print(message)

message = message.center(50,'*') # Karakter dizisini 50 karakterlik bir alanda ortalar,boşluklara * koyar.
print(message)
