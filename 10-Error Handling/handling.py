# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# # except ZeroDivisionError:
# #     print('y için 0 girilemez')
# # except ValueError:
# #     print('x ve y için sayısal değer girmelisiniz')
# # except ValueError,ZeroDivisionError:
# #     print('Hata')
# # except (ValueError,ZeroDivisionError) as e:
# #     print('Hata')
# #     print(e)
# except:
#     print('Hata')
# else: 
#     print('Her şey yolunda')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as e:
        print('Hata')
        print(e)
    else:
        break
    finally:
        print('try except sonlandı')    
