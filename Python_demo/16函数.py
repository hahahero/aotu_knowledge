#1、便于管理python代码
#2、方便其它系统调用
#3、代码可维护性高
def 函数名():
    for i in range(1, 10):  # 打印行数
        for j in range(1, i + 1):  # 打印行内容
            print(f'{j}*{i}={j*i}', end='\t')
        print()

a = 函数名()
print(a)