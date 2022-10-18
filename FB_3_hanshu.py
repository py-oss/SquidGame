# 尽量避免写重复的代码，少复制粘贴，也就是所谓的DRY原则——Don't Repeat Yourself。

# 函数：“喂”给函数一些数据，它就能内部消化，执行相应的功能，最终给你“吐”出你想要的东西

# 定义
'''
def 变量（参数）：
    函数体
    return 语句
'''
# 函数名：1. 名字最好能体现函数的功能，一般用小写字母和单下划线、数字等组合
#         2. 不可与内置函数重名（内置函数不需要定义即可直接使用）
def math(x):
# 参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同
# 规范：括号是英文括号，后面的冒号不能丢
    y = 3*x + 5
# 函数体：函数的执行过程，体现函数功能的语句，要缩进，一般是四个空格
    return y
# return语句：后面可以接多种数据类型，如果函数不需要返回值的话，可以省略

# 调用
a = math(10)
print(a)
# 练习：返回字符串的长度，1. 设置一个初始为0的计数器；2.遍历字符串，每遍历一次，计数器加一；3.返回计数器的值
def str_len(x):
    j = 0
    for i in x:
        j += 1
    return j
    print(j)
str_len('三根皮带，四斤大豆')

# 参数类型
'''
位置参数：按照对应参数的位置顺序传递数据
默认参数：直接在定义函数的时候给参数赋值，默认参数必须放在位置参数之后，默认参数可以改变
不定长参数：传递给参数的数量是可选的、不确定的，格式比较特殊，是一个星号*加上参数名，它的返回值也比较特殊，是一个元组
'''
def menu(*barbeque): # 带*号为不定长参数
    return barbeque
order = menu('烤鸡翅','烤茄子','烤玉米')
#括号里的这几个值都会传递给参数barbeque
print(order)
print(type(order))
'''
>>> ('烤鸡翅', '烤茄子', '烤玉米')
>>> <class 'tuple'>
'''

# 返回多个值
# 要返回多个值，只需将返回的值写在return语句后面，用英文逗号隔开即可
from calendar import c
import random 
appetizer = ['话梅花生','拍黄瓜','凉拌三丝']
def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 < money < 10:
        b = random.choice (appetizer)
        return b, '溏心蛋'
print(coupon(6))
print(type(coupon(6)))
dish, egg = coupon (7) # 可以同时定义多个变量，来接收元组中的多个元素
# 元组的两个元素分别赋值给变量dish和egg
print(dish)
print(egg)
'''
>>> ('凉拌三丝', '溏心蛋')
>>> <class 'tuple'> # 返回值为元组
'''

# 变量作用域
# 第一点：一个在函数内部赋值的变量仅能在该函数内部使用（局部作用域），它们被称作【局部变量】
# 第二点：在所有函数之外赋值的变量，可以在程序的任何位置使用（全局作用域），它们被称作【全局变量】
rent = 3000
def cost():
    global variable_cost # global语句，将局部变量声明为全局变量，一般写在函数体第一条
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    variable_cost = utilities + food_cost
    print('本月的变动成本是' + str(variable_cost))
def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))
cost()
sum_cost()

# 函数嵌套
# 优秀的函数应该计算逻辑和运行逻辑分开，再加上抛出异常
# def语句后的代码块只是封装了函数的功能，如果没有被调用，def语句后的代码永远不会被执行
def div(num1, num2): # 计算逻辑
    growth = (num1 - num2) / num2
    percent = str(growth * 100) + '%'
    return percent
def warning(): # 异常抛出
    print('Error: 你确定上个月一毛钱都不赚不亏吗？')
def main(): # 运行逻辑
    while True:
        num1 = float(input('请输入本月所获利润'))
        num2 = float(input('请输入上月所获利润'))
        if num2 == 0:
            warning()
        else:
            print('本月的利润增长率：' + div(num1,num2))
            break
main()

### 练习1，计算工资
def salary(time):
    if time < 6:
        salary = 500
        return salary
    elif 6 < time <= 12:
        salary = time * 120
        return salary
    else:
        salary = time * 180
        return salary
def warning():
    print('你一天都没工作过还想拿工资')
def main():
    time = int(input('请问你工作了多少个月：'))
    if time <= 0:
        warning()
    else:
        pay = salary(time) # 调用函数不要忘记括号，返回值必须要有一个变量接收，才能打印出来
        print('该员工来了 {} 个月，获得奖金 {} 元'.format(time,pay))
main()

### 练习2，将下列代码用函数封装
# 查看注释，运行代码。
import random
import time
# 用random函数在列表中随机抽奖，列表中只有3位候选者。
luckylist = ['海绵宝宝','派大星','章鱼哥']
# random模块中有个随机选取一个元素的方法：random.choice()。
a = random.choice(luckylist)  # 从3个人中随机选取1个人。
print('开奖倒计时',3)
time.sleep(1)  # 调用time模块，控制打印内容出现的时间
print('开奖倒计时',2)
time.sleep(1)
print('开奖倒计时',1)
time.sleep(1)
# 使用三引号打印hellokitty的头像
image = '''
 /\_)o<
|      \\
| O . O|
 \_____/
'''
print(image)  # ……
print('恭喜'+a+'中奖！')  # 使用print函数打印幸运者名单

# 没有运行结果，谁能告诉我这个代码错误在哪里——原来是没调用函数，一定要调用啊
import random
import time
def candidate():
    a = input('第一个候选人是：')
    b = input('第一个候选人是：')
    c = input('第一个候选人是：')
    luckylist = [a,b,c]
    d = random.choice(luckylist)
    return d
def warning():
    print('你输入的不是一个人名哦~')
def main():
    z = candidate()
    print('开奖倒计时',3)
    time.sleep(1)
    print('开奖倒计时',2)
    time.sleep(1)
    print('开奖倒计时',1)
    time.sleep(1)
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)
    print('恭喜{}中奖！'.format(z))
main()