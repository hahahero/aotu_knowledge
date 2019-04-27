"""
1 * 1 = 1
1 * 1 = 1   1 * 2 = 2
1 * 1 = 1   1 * 2 = 2   1 * 3 = 3
"""
# 打印结构，矩形
for i in range(9):  # 打印行数
    for j in range(9):  # 打印行内容
        print('*', end='\t')
    print()  # 打印为空，默认换行

# 打印结构，三角形
for i in range(1, 10):  # 打印行数
    for j in range(i):  # 打印行内容
        print('*', end='\t')
    print()

for i in range(1, 10):  # 打印行数
    for j in range(i):  # 打印行内容
        print('{}*{}={}', end='\t')
    print()

# 打印99乘法表
for i in range(1, 10):  # 打印行数
    for j in range(1,i+1):  # 打印行内容
        print(f'{j}*{i}={j*i}', end='\t')
    print()
