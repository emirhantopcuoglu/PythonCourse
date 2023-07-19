# dictionary = {'key' : 'value'}

cities = {14 : 'Bolu',34 : 'İstanbul',6 : 'Ankara',}
print(cities[14])

users = {
   'ahmet': {
        'age' : 5,
        'roles': ['user'],
        'email' : 'ahmet@gmail.com',
        'phone' : 12313213123
    },

    'mehmet': {
        'age' : 12,
        'roles': ['admin','user'],
        'email': 'mehmet@gmail.com',
        'phone' : 32423424
    }
}
print(users['ahmet'])
print(users['mehmet']['age'])
print(users['mehmet']['roles'][0])



