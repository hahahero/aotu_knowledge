'''
包裹传参分为两种：
1、包裹位置传参 *
2、包裹关键字传参 **
'''
def a1(*all): #形参（形式参数）
    print(type(all))
    print(all)

a1(12,2,3,2,1,23,4,5,6,7)
a1(2,3,4)
#包裹关键字传参
def a2(**alls):
    print(type(alls))
    print(alls)

a2(x=100,y=50)
