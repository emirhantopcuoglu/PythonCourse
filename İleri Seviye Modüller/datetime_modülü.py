from datetime import datetime
from datetime import timedelta

now = datetime.now()
result = datetime.now()
result = datetime.today() # now() ve today() aynı işi yapıyor.
result = now.year
result = now.month
result = now.day
result = now.hour
result = now.minute
result = now.second
result = datetime.ctime(now) # daha detaylı bilgi verir
result = datetime.strftime(now,'%Y') # yıl
result = datetime.strftime(now,'%X') # saat
result = datetime.strftime(now,'%d') # gün
result = datetime.strftime(now,'%A') # gün (string)
result = datetime.strftime(now,'%B') # ay (string)
print(result)

t = '23 October 2022 hour 19:19:30'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt)

birthday = datetime(2002,6,6,12,30,45)
print(birthday)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0) # bilgisayarlar için milat bilgisi
result = now - birthday # timedelta
#result = result.days # gün bilgisi
result = result.seconds # saniye bilgisi

result = now + timedelta(days=3)

print(result)


