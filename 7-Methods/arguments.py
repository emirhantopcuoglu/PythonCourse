def changeName(n):
    n = "ali"
name = "yağmur"
changeName(name)
print(name)  

def changeList(l):
    l[0] = "Istanbul"
list1 = ["ankara","izmir"]
changeList(list1)
print(list1)

def add(*params):
    return sum((params))

print(add(15,20))
print(add(5,15,27,49,53))

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(5,15,35,65,87,key1 = "value1",key2 = "value2")






    



