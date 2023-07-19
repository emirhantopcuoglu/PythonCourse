# Class
class Person:
    
# class attributes
    adress = 'no information'
# object attributes
    def __init__(self,name,year):
        self.name = name # self yerine this kullanılabilir.
        self.year = year
        print("init metodu çalıştı.")
# methods
    def intro(self):
        print('Hello ' + self.name)
    def calculateAge(self):
        return 2022 - self.year
# object (instance)
p1 = Person('Ali', 1990)
p2 = Person('Eylül', 1995)
# updating
p1.name = 'Ahmet'
p1.adress = 'Istanbul'
# accessing object attributes
print(f'name: {p1.name} year: {p1.year} address: {p1.adress}')
print(f'name: {p2.name} year: {p2.year} address: {p2.adress}')

print(type(p1))
print(type(p2))

p1.intro()
p2.intro()
print(f'{p1.name} yaş: {p1.calculateAge()}')
print(f'{p2.name} yaş: {p2.calculateAge()}')


