website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python programlama rehberiniz (40 saat)"

# course karakter dizisinde kaç eleman bulunur?
print(len(course))

# website karakter dizisinin içinden www karakterlerini alın.
print(website[7:10])

# website içinden com karakterlerini alın.
length = len(website)
print(website[length-3:length])

# course içinden ilk 15 ve son 15 karakteri alın.
print(course[0:15])
print(course[-15:])

# course ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])

name,surname,age,job = "Bora","Yılmaz",32,"Mühendis"

# Yukarıda verilen değişkenlerle aşağıdaki ifadeyi ekrana yazdırın.
# Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.

print(f"Benim adım {name} {surname},yaşım {32} ve mesleğim {job}")

# 'Hello world' ifadesindeki w'yi "W" ile değiştirin.
s = "Hello world"
s = s[0:5] + " W" + s[-4:]
print(s)

# 'abc' ifadesini yan yana 3 defa yazdırın.
print("abc"*3)
