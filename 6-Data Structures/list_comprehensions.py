# for x in range(10):
#     print(x)

# numbers = [x for x in range(10)]
# print(numbers)

# numbers = []
# for x in range(10):
#     numbers.append(x)

# for x in range(10):
#     print(x**2)

# numbers = [x**2 for x in range(10)]
# print(numbers)

# numbers = [x*x for x in range(10) if x%3 == 0]
# print(numbers)

# myString = 'Hello'
# myList = []
# for char in myString:
#     myList.append(char)
# print(myList)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)