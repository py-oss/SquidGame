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
# 1. 积累生活经验
# 2. 提出产品需求
    # a. 替代重复性劳动
    # b. 制作工具解决问题
# 3. 形成技术方案
    # a. 分析问题，明确结果
    # b. 思考需要的知识，或学习新知识
    # c. 思考切入点
    # d. 尝试解决问题的一部分
    # e. 重复以上步骤
# 4. 完成程序代码

# 当我吃午饭时，我在吃些什么
# 我的设计
import random
caidan = []
y = 0
while True:
    a = input('请输入你今天想吃的菜，输入0不加菜了：')
    caidan.append(a)
    if a == str(y):
        break
i = random.randint(0,3)
print(caidan)
print(caidan[i])
# 老师的设计
import random
list_food = ['KFC', '蒸菜馆', '楼下快餐店', '桂林米粉', '东北饺子', '金牌猪脚饭', '三及第汤饭']  # 备选菜单，可自定义。
list_choice = [] # 将需要用到的表格和变量放在开头
def choose(list): # # 由于两个原因都包含判断过程，所以，为了让代码更简洁，可将其封装成函数。
    while True:
        food = random.choice(list)
        judgement = input('去吃【%s】好不好啊？同意的话输入y，不想吃直接回车即可。'%(food))
        if judgement == 'y':
            print('去吃【%s】！就这么愉快地决定啦！'%(food)) 
            break
reason = int(input('你不知道吃什么的原因是：1.完全不知道吃什么；2.在几家店之间徘徊（请输入1或2）：')) # 判断环节
if reason == 1:
    choose(list_food)
elif reason == 2:
    add = True
    while add:
        choice = input('请输入让你犹豫的店名（注：一家一家输，完成后输入y）：')
        if choice != 'y':  # 这个判断语句，是为了不将 y 也添加到菜单里。
            list_choice.append(choice)
        if choice == 'y':
            add = False
    choose(list_choice)          
else:
    print('抱歉，目前还不支持第三种情况——不过，你可以加代码哦。')

# 滚动的广告牌
import os, time
def main():  # 用函数封装，可复用性会高一些（可在其他的.py文件里调用该函数。）
    content = ' 风变编程，陪你一起学Python '  # 广告词可自定义。
    while True: # 运行前可改为 for i in range(20) 控制一下循环次数。
        # linux/os x系统【清除屏幕】代码（线上使用本代码）
        os.system('clear')  # 清屏和打印结合起来，形成滚动效果。
        # windows系统【清除屏幕】代码
        '''
        os.system('cls') 
        '''
        print(content)
        content = content[1:] + content[0]  # 这行代码相当于：将字符串中第一个元素移到了最后一个。
        time.sleep(0.25)  # 你可以改下时间，体会“循环周期”和“滚动速度”之间的关联。
if __name__ == '__main__':  # 类里面学到的检测方法，在函数中其实也可以用。
    main()