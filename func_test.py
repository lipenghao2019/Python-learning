#print('abc',end='\n')
# print('abc')
#
# def func(a,b,c):
#     print('a= %s' %a)
#     print('b= %s' %b)
#     print('c= %s' %c)
#
# func(1,2,3)

#取得参数的个数
# def howlong(first, *other):
#     print( 1 + len(other))
#
# howlong()

var1 = 123

def func():
    global var1
    var1 = 456
    print(var1)

func()
print(var1)


