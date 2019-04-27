"""
1、break:跳出循环，不再执行
Python break语句，就像在C语言中，打破了最小封闭for或while循环。
break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
break语句用在while和for循环中。
如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。
2、continue：跳出本次循环，执行下一次
Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
"""
for i in range(100):
    if i == 50:
        continue
    if i == 60:
        break
    print(i)

while True:
    if i == 10:
        continue
    if i == 20:
        break
