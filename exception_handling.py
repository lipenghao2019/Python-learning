#i = j

#print())

#a='123'
#print(a[3])

# d = {'a':1 , 'b':2}
# print(d['c'])

#year = int(input('input year:'))

# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('年份要输入数字')

#a=123
#a.append()

#except (ValueError,ArithmeticError,KeyError)

#try:
#    print(1/0)
#except ZeroDivisionError as e:
#    print('0不能做除数 %s' %e)

# try:
#     print(1/'a')
# except TypeError as e:
#     print('a不能做除数 %s' %e)

# try:
#      print(1/'a')
# except Exception as e:
#      print('%s' %e)

# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')

try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()