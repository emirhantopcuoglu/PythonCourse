name = "Sadık"
surname = " Turan"
age = 36
greeting = "Hello,my name is " + name + surname + " I am " + str(age) + " years old."
length = len(greeting)
print(greeting)
print(greeting[0])
print(len(greeting)) #kaç karakter olduğunu gösterir
print(greeting[length-1])
print(greeting[-1])
print(greeting[2:5]) #2'den başlar 5 e kadar gider,5 dahil değil
print(greeting[2:]) #2'den başlar sona kadar gider
print(greeting[:5]) #en baştan 5'e kadar gider
print(greeting[2:40:2]) #2'den başlar 40'a kadar ikişer ikişer gider