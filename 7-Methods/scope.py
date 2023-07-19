# x = 'global x'

# def function():
#     x = 'local x'

# function()
# print(x)

x = 50 
def test():
    global x 
    print(f'x : {x}')
    x = 100
    print(f'changed to {x}')
test()
print(x)