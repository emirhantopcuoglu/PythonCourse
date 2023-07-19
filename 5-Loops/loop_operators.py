# range(başlangıç,bitiş,artış miktarı)

# for item in range(10):
#     print(item)

# for item in range(1,10):
#     print(item)

# for item in range(0,100,5):
#     print(item)

# print(list(range(50,100,20)))

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)
