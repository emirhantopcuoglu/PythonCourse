website = 'www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)'

# ' Hello World ' baş ve sondaki boşlukları silin.
x = ' Hello World '
x = x.strip()
print(x)

# 'www.sadikturan.com' içindeki sadikturan hariç tüm karakterleri silin.
x1 = 'www.sadikturan.com'
x1 = x1.replace('www.','')
x1 = x1.replace('.com','')
print(x1)

# course'daki tüm harfleri küçük yapın.
course = course.lower()
print(course)

# website içinde kaç tane a vardır?
result = website.count('a')
print(result)

# website içerisinde '.com' ifadesi var mı?
index = website.find('.com')
print(index)

# website 'www' ile başlayıp 'com' ile bitiyor mu?
x2 = website.startswith('www')
print(x2)
x2 = website.endswith('com')
print(x2)

# course içerisindeki karakterlerin hepsi alfabetik mi?
course = course.isalpha()
print(course)

# 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin.
message = 'Contents'.center(50,'*')
print(message)

# course'daki tüm boşlukları '-' ile değiştirin.
#result2 = course.replace('','-')
#print(result2)

# 'Hello World' World ifadesini 'There' olarak değiştirin.
x3 = 'Hello World'.replace('World','There')
print(x3)



