import re
# Regular Expressions

str = 'Python Programming | 40 Hours'
# re.findall():
# result = re.findall("Python",str) # string ifadeyi bulur
# result = len(result) # string ifadenin sayısı

# re.split():
# result = re.split(" ",str) # string ifade boşluk karakterlerinden bölünür

# re.sub():
# result = re.sub(" ","-",str) # boşluk karakterlerini - ile değiştirir
# result = re.sub("\s","-",str) # boşluk karakterlerini - ile değiştirir

# re.search():
# result = re.search("Python",str) # string ifadeyi arar
# result = result.span() # bulunan string ifadenin ilk ve son indexini yazar
# result = result.start() # string ifadenin ilk indexini yazar
# result = result.end() # string ifadenin son indexini yazar
# result = result.group() # bulduğu ifadeyi geri döndürür
# result = result.string # string ifadeyi nerede aradığını döndürür

"""
[] Köşeli parantezler arasına yazılan bütün karakterler aranır.
örn:    [abc] --> a : 1 match
              --> ac : 2 match
              --> Python : no matches
[a-e] --> [abcde]
[1-5] --> [12345]

[^abc] --> abc hariç harfler
[^0-9] --> rakam olmayan karakterler

"""
# result = re.findall("[P]",str) # Bulunan P harflerini liste içinde döndürür

# result = re.findall("[a-e]",str) # a-e arası harfleri arar
# result = re.findall("[0-4]",str) # 0-4 arası rakamları arar

# result = re.findall("[^0-9]",str)

"""
    . --> Herhangi bir tek karakteri belirtir.
        .. -->  a = no matches
                ab = 1 match
                abc = 1 match
                abcd = 2 matches

"""
# result = re.findall("...",str) # ifadeleri 3 karakterli döndürür
# result = re.findall("Py..on",str)

"""
    ^x --> Belirtilen karakterle başlıyor mu?
        ^a -->  a: 1 match
                abc: 1 match
                bc: no matches

"""
# result = re.findall("^P",str)

"""
    x$ --> Belirtilen karakterle bitiyor mu?
        a$ -->  a: 1 match
                lamba : 1 match
                Python : no matches

"""
# result = re.findall("s$",str)
# result = re.findall("Hours$",str)

"""
    *x Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
        ma*n -->    mn : 1 match
                    man : 1 match
                    maan : 1 match
                    main : no matches
"""
# result = re.findall("Hof*urs",str)

"""
    +x Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
        ma+n -->    mn : no matches
                    man : 1 match
                    maan : 1 match
                    main : no matches
"""
result = re.findall("Ho+urs",str)

"""
    {} karakter sayısını kontrol eder
        al{2} a'dan sonra l 2 kez tekrarlamalı
        al{2,3} a'dan sonra l en az 2, en fazla 3 kez tekrarlamalı
        [0-9]{2,4} en az 2, en fazla 4 basamaklı sayılar 
"""
# result = = re.findall("[0-9]{2}",str) SYNTAX ERROR ?

print(result)