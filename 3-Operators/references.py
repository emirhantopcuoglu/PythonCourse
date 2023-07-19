# value types -> string,number
x = 5
y = 25
x = y
y = 10
print(x,y)

# reference types -> list
a = ['istanbul','ankara']
b = ['istanbul','ankara']
a = b 
b[0] = 'izmir'
print(a,b)
a[0] = 'antalya'
print(a,b)