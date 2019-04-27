# 函数的返回值有什么作用？方便其它值取值定义好的函数return
def sum(a, b):
    c = a + b
    return a,b,c

a = sum(12,22)
print(a)
