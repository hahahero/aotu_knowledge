#函数解包裹
#解包裹，位置传参
def a2(a,b,c): #形参
    print(a,b,c)

args = (2,3,4)
a2(*args)

args2 = {'a':5,'b':6,'c':7} #实参
a2(**args2)