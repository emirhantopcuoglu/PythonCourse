fruits = {'banana','apple','orange'}

# print(fruits[0]) -> indekslenemez!

fruits.add('cherry')
fruits.update(['mango','grape','apple']) # aynı eleman tekrar eklenmez
print(fruits)

myList = [1,2,3,3,4,4,5]
print(myList)
print(set(myList))

fruits.remove('apple')
fruits.discard('mango')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)