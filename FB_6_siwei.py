# 高效学习
# 打印九九乘法表
# 基础知识在，但逻辑思维不在的我的做法
for x in range(1,10):
    for y in range(1,10):
        if x > y:
            pass
        else:
            z = x*y
            if y == 9:
                print('{} * {} = {}'.format(x,y,z))
            else:
                print('{} * {} = {}'.format(x,y,z),end=' ') # 不换行，末尾拼接一个空格
# 老师的做法，总是感觉更智能
for i in range(1,10):
    for j in range(1,i+1):
        print('{} * {} = {}'.format(i,j,i*j),end = ' ')
    print('')
# 合并两班成绩并排序，涉及到新知识需要用百度查询大法，一步步验证、排查并直到得出结果
a = [91, 95, 97, 99]
b = [92, 93, 96, 98]
a.extend(b)
a = sorted(a)
print(a)
# 学完库的知识再来补齐
# 计算平均分，低于平均分打印出来
from numpy import *
a = [91, 95, 97, 99]
b = [92, 93, 96, 98]
a_avg = mean(a)
b_avg = mean(b)
print('{} , {}'.format(a_avg,b_avg))

# 代码报错
# SyntaxError指的是语法错误
# 方法：要用句点.调用
# 解决思路不清的bug：1 - 活用print()函数；2 - 用#注释部分代码
# 多行注释快捷操作，选中代码后使用快捷键操作：Windows快捷键是ctrl+/，Mac为cmd+/
# 异常处理机制：可以在异常出现时即时捕获，然后内部消化掉，让程序继续运行
print('\n欢迎使用除法计算器！\n')
while True:
    try:
        x = input('请你输入被除数：')
        y = input('请你输入除数：')
        z = float(x)/float(y)
        print(x,'/',y,'=',z)
        break  # 默认每次只计算一次，所以在这里写了 break。
    except ZeroDivisionError:  # 当除数为0时，跳出提示，重新输入。
        print('0是不能做除数的！')
    except ValueError:  # 当除数或被除数中有一个无法转换成浮点数时，跳出提示，重新输入。
        print('除数和被除数都应该是整值或浮点数！')
    # 方式2：将两个（或多个）异常放在一起，只要触发其中一个，就执行所包含的代码。
    # except(ZeroDivisionError,ValueError):
    #     print('你的输入有误，请重新输入！')
    # 方式3：常规错误的基类，假设不想提供很精细的提示，可以用这个语句响应常规错误。
    # except Exception:
    #     print('你的输入有误，请重新输入！')
# 当你运行两次代码后，你就知道：try下面可以包含多个except，针对不同的报错，类似多个 elif。

# 构思产品