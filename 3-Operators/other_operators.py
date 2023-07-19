# identity operator: is
from tkinter import N


x = y = [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z)
print(x is y)
print(x is not y)
print(x is z)

# membership operator: in
a = ['apple','banana']
print('banana' in a)

name = 'Python'
print('P' in name)
print('p' not in name)