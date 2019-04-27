# if (判断条件1):
#     pass
# elif (判断条件2):
#     pass
# elif (判断条件3):
#     pass
# else:
#     pass
a = 100
if a >= 90:
    print("考试很好成绩")
elif a >= 80:
    print("考试一般般")
elif a >= 60:
    print("考试及格")
else:
    print("考试太差了")

if result['status'] == 200:
    print("接口测试成功")
elif result['status'] >= 301:
    print("库存不及的错误提示")
elif result['status'] >= 404:
    print("接口报错")
else:
    print("系统异常")