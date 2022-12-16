# SquidGame

[TOC]

## 1、数据类型

### 与计算机对话

#### print()函数 功能：打印内容

```python
print(520) # 无引号用法：计算结果
print('千与千寻') # 单引号用法：原样输出
print("let's go") # 双引号+单引号：区分结构
print('''
人总是缺乏
第一次做好的耐心和远见
却总是
有耐心和能力一次次返工
''') # 代码内换行
print('离离原上草\n一岁一枯荣') # 代码内换行
```

#### input()函数 功能：输入数据

- 有问有答，有来有往；
- 函数好用，赋值第一；
- 返回类型，必为str
- 想要整数，源头转换

```python
magic = input('请在以下选项【厄里斯魔镜；时间转换器；飞天扫帚；隐形斗篷】中，选择出你最想拥有的魔法物品：')
print(magic+'是我最想拥有的魔法！')
```

### 构成虚拟世界的原子

#### 变量

**变量必须先声明并赋值才能使用**

```python
a = 5 # 赋值用【=】号表示
b = 10
a = b # 变量命名要规范
print(a) # 变量的最终值等于最后赋值的值
```

### 当我使用Python时，我在使用什么

#### 数据类型

只要被引号（单引号/双引号/三引号）括起来的数据都是字符串，用`str`表示

没有小数点的数字统称为整数，运算结果永远精确，用`int`表示

有小数点的数字统称为浮点数，运算有四舍五入的误差，用`float`表示

#### 数据拼接：+

只能拼接字符串类型的数据，其他数据类型不能拼接——“圈子不同，不能相融”

#### type()函数

作用：查询数据类型

语法：

```python
print(type('放入需要查询的数据'))
```

#### 布尔值 True 和 False

1. 计算机判断真假的过程叫做布尔运算
2. 布尔运算会产生`【True】`和`【False】`的布尔值
3. True和False就像开关，决定`if语句、while语句`是否运行

#### bool()函数 用来判断数据的真假，和type()的用法类似

```python
print(bool(''))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(None))
```

#### 列表 适用所有增删查改语句：左右空，取到头；左要取，右不取

##### 靠“偏移量”取值，可迭代对象，可用for……in……循环来遍历

- **列表名** 命名需能一眼判断是什么数据
- **赋值号** 将列表内的数据赋值给变量
- **中括号** 用中括号区分列表的整体数据结构
- **逗号** 用逗号间隔列表内元素

```python
students = ['晓敏',18.8,42] # 列表很包容，字符串/整数/浮点数都可以放进去
print(type(students))
print(type(students[0]))
print(type(students[1]))
print(type(students[2]))
```

##### 增
```python
students = ['晓敏',18.8,42]
students.append(['小米','小美'])
print(students)
```

给列表增加元素语法为：`列表名.append(元素)`

append()函数只能追加一个元素进去

该元素可以是字符串/整数/浮点数/列表

因此，列表理论上长度可变，容量无限

##### 删
```python
del students[0] # del 列表名[元素索引]
print(students) # del 列表名 可以删除整个列表
del students['小米'] # del 无法直接删除指定的某元素，必须通过元素的索引才能操作
print(students) # 报错：类型错误。 只能是整数或者切片，不能使用字符串
```

##### 查：切片， 将列表的某个片段拿出来处理，切片后的列表也是列表
```python
students = ['晓敏',18.8,42]
print(students[:])
print(students[0:1])
print(students[1:])
print(students[:1])
print(students[1:2])
print(students[:0]) # 超出列表范围取出来为空列表
print(type(students[3:])) # 空列表也是列表
```

##### 轮流排座问题

###### pop()函数用法
```python
print('提取只取不删：')
list1 = ['0','1','2','3']
print(list1[3])
print(list1)

print('\n删除(del)只删不取：' )
list1 = ['0','1','2','3']
del list1[3]
print(list1)

print('\n移除（pop）又取又删：')
list1 = ['0','1','2','3']
print(list1.pop())  # 默认删除最后一个元素，并返回该元素的值。
print(list1)
print(list1.pop(0))  # 也可指定删除某个元素，并返回该元素的值。
print(list1)

zuowei = ['小明','小红','小刚']
for i in range(3): # 循环第一步，永远先确定次数是否明确，决定选择那种循环方法
    zuowei1 = zuowei.pop(0) # 要传数值0进去，因为逻辑是删除第一个并取值；不加0则是删除最后一个并取值，底下就变成继续追加进末尾，结果自然相同
    zuowei.append(zuowei1)  # 之后将上面取到的值追加近新列表里面
    print(zuowei)
```

#### 字典

##### 靠“键”取值，可迭代对象，可用for……in……循环来遍历
- **字典名** 需要一眼知道命名用来做什么
- **赋值号** 将数据赋值给变量
- **花括号** 用来区分字典的整体数据结构
- **逗号** 用来区分字典内的数据结构
- **冒号** 字典内的单个元素数据是由键值对组成，用冒号区分开键值

```python
scores = {'小明':96,'小红':90,'小刚':90}
print(len(scores)) # len()函数可以取得字典或列表的长度
```

字典的键是唯一的，值可以重复；如果命名了相同的键，后面的值会覆盖前面的值

##### 增
```python
scores ['小艺'] = 66 # 字典名[键] = 值
print(scores) # 可直接在字典末尾追加一行数据
```
##### 删
```python
scores = {'小刚':60,'小明':88,'小红':22}
del scores['小刚'] # del 字典名[键] 即可删除指定的键值对
print(scores)
```
##### 查
```python
scores = {'小静':28,'小张':99,'小怡':87}
print(scores['小张'])
print(scores[0]) # traceback回溯错误，发现keyerror键错误，证明字典取值只能靠键
```
##### 改
```python
scores ['小明'] = 92 # 字典名[键] = 值
scores ['小红'] = 72 # 可修改指定键的值
print(scores) # 上述区别在于，已存在的会覆盖新的键值对；不存在的会在末尾追加新的键值对
```

#### 列表和字典对比
1. 修改都用同样的赋值语句
2. 都支持任意嵌套，可嵌套数据可以是列表也可以是数据

```python
scores1 = [18,19,20]
scores2 = [19,20,18]
print(scores1 == scores2) # 列表有序，偏移定位
scores3 = {'小明':167,'小刚':188,'小红':158}
scores4 = {'小红':158,'小明':167,'小刚':188}
print(scores3 == scores4) # 字典无序，键来取值
```

#### 元组 可迭代对象，可用for……in……循环来遍历

将数据放在小括号()中，它的用法和列表用法类似，主要区别在于：列表中的元素可修改，元组中的元素不可更改。

```python
tuple1 = ('晓敏',18.8,42)
for i in tuple1:
    print(i)
```

#### 数据转换

##### str() 将其他数据类型转换成字符串

```python
b = 42
print(type(str(b)))
print(type('42')) # 也可以直接使用引号转换为字符串
```

当我们使用引号时，引号里的东西，都会被强制转换为字符串格式

如果引号内放入变量名b，将被强制转换为字符串的是b，而不是数字42

##### int() 只有符合整数规范的数据可以被转换成整数，浮点数会强制取整转换
```python
number1 = '1'
number2 = '2'
print(int(number1)+int(number2))
print(type(int(number1)))
print(type(int('2')))
print(int(3.8))
```

浮点数也被int()函数强制转换，但会直接抹零取整数，比如上面的代码输出结果为 3

```python
print(int('1.55'))
```

文本类和小数类字符串无法被转换；以上代码会报错，无法转换

##### float() 可将整数和符合数字规范的字符串转换为浮点数
```python
print(type(188))
print(type(float(188)))
```

#### 格式化字符串
`%` 格式化：`str % ()`

```python
print('%s%d'%('数字：',0))
print('%d，%d'%(0,1))
print('%d，%d，%d'%(0,1,0))
```

`%f`的意思是格式化字符串为浮点型，`%.1f`的意思是格式化字符串为浮点型，并保留`1`位小数。

```python
name1 = 'Python'
print('I am learning %s'% name1)  # 注：当只跟一个数据时，%后可不加括号，format()一定要有。
```

`format()`格式化函数：`str.format()`

```python
print('\n{}{}'.format('数字：',0))  # 优势1：不用担心用错类型码。
print('{}，{}'.format(0,1))  # 不设置指定位置时，默认按顺序对应。
print('{1}，{0}'.format(0,1))  # 优势2：当设置指定位置时，按指定的对应。
print('{0}，{1}，{0}'.format(0,1))  # 优势3：可多次调用format后的数据。

name2 =  'Python基础语法'
print('我正在学{}'.format(name2))  # format()函数也接受通过参数传入数据。
```

## 2、循环

## 条件判断 在什么条件下，该去做什么

### 单向判断：if
#### 如果……就……
```python
stonenumber = 6
if stonenumber >= 6: # 冒号
    print('毁灭宇宙') # 缩进（4个空格或一个tab），if条件下内部命令
    # （条件）冒号+（命令）缩进，区分代码之间的层次，理解条件执行的逻辑和先后顺序
# if(条件满足):
#    运行结果
```

### 双向判断：if……else……
#### 如果……不满足……就……
```python
stonenumber = 3
if stonenumber >= 6: # 与 18AD6C21.png 的条件互斥
    print('毁灭宇宙')
else:
    print('找到其他宝石')   
```

### 多向判断：if……elif……else
#### 别把鸡蛋放在一个篮子里，要做好两手准备；如果条件不满足时，我们该怎么办
```python
stonenumber = 0
if stonenumber >= 6:
    print('世界毁灭')
elif 0 < stonenumber < 5:
    print('毁掉宝石')
else:
    print('穿越时空，回到过去')
# elif后面可不接else；所有条件相互之间为互斥关系
```

### if嵌套
```python
# 扒洋葱大法：
# 1. 写基础条件
# 2. 写基础条件1的额外条件
# 3. 写基础条件2的额外条件
chengji = 26
if chengji >= 60:
    print('成绩及格')
    if chengji >= 80:
        print('成绩优秀')
    else:
        print('成绩一般')
else:
    print('成绩不及格')
    if chengji < 30:
        print('平时不认真，属于学渣')
    else:
        print('还行吧，努力下还能及格')
print('程序结束')
```

## 循环

### for……in……循环，遍历数据；叫号-排队-办事
```python
list1 = [1,2,3,4,5] # 叫号排队 i是变量名，在叫号；列表是排队的人
for i in list1: # 排队的人可以是字符串、列表、字典；整数和浮点数不能排队
    print(i) # 冒号和缩进区分代码块，下面的代码是执行的命令，也即办事流程

dist1 = {'小明':'醋','小红':'油','小白':'盐','小张':'米'}
for a in dist1: # 原来叫的这个号这么随便，只要在for……in循环内，就默认a是字典内的键
    print(dist1[a]) # 换成b、c就报错未定义；所以只要在for……in循环内，“叫号”的这个变量无需声明即可直接使用
```

#### range()函数 取头不取尾的整数序列
```python
for i in range(-1,3):
    print('做咩啊')
for i in range(-2,10,2): # 从-2取到9，步长为2；第1个元素不填时，默认从0开始
    print(i)
for i in range(1,5):
    i = i * 5
    print(i)
```

### while循环 无条件，不办事；过-办事
```python
# 定义变量
# 给出条件
# 执行命令

i = 0
while i < 5: # 条件满足时，不停的办事；一旦条件不满足，就不再循环这串代码
    i = i + 1 # 冒号+缩进，区分代码块；缩进子句为办事流程
    print(i) # 循环只在代码块内循环，不会跳到i=0去，因为程序从上到下执行

code = ''
while code != 816:
    code = int(input('请尝试输入密码：')) # 用int()强制转换了，终端只能输入整数类型了，不然报错；实际开发中放行条件用字符串更合适
    print('密码输入错误，请重试！')
print('欢迎回家！')

a = 1
while a < 6:
    b = a * 5 # 这一步错误的用了for……in循环，导致5/10/15/20/25输出了5次；这里实际就是简单的乘法即可解决
    print(b) # 引入第2个变量，要理清楚两个变量之间的关系；同理，变量之间的逻辑关系理清楚，办事流程就清楚
    # print(a*5) 着相了，直接输出a*5更方便
    a = a + 1 # 或者说，根据办事流程，来判定变量间的关系
```

### for…in…与while循环的使用区别
```python
for i in range(1,8): # 循环次数明确，用for……in
    if i != 4:
        print(i)

i = 1
while i < 8:         # 循环次数不明确，用while
    if i != 4:
        print(i)
    i = i + 1
```

## 四种循环子语句

- break 从循环内跳出
- continue 跳到循环开头
- pass 什么都不做
- else 循环语句后，如果没有遇到break就执行else语句

```python
#1
for i in range():
    if ...:
        break
# if...break... 只能在循环内部使用，意思是：如果满足某种条件，就提前结束循环

while True:
    a = input('小龙女来了吗')
    if a == '来了':
        break
print('小龙女终于可以出来了')
```
```python

#2
while...():
    ...
    if ...:
        continue
    ...
# if...continue... 只能在循环内部使用，意思是：当某个条件被满足，触发continue语句，将跳过之后的代码，直接回到循环的开始

for i in range(5):
    print('明日复明日')
    if i == 3:
        continue
print('当i等于3这句话打印不出来')
```

```python
#3
a = int(input('请输入一个整数：'))
if a > 100:
    pass
else:
    print('你输入了一个小于100的数字')

# pass...表示一个占位，即：什么都不做
```

```python
#4
while...():
    ...
else:
    ...
# else...代表其他条件

i = 0
while i < 5:
    a = int(input('请输0结束循环，你有5次机会：'))
    i = i + 1
    if a == 0:
        print('你触发了break语句，导致else语句不会生效')
        break
else:
    print('5次循环你都错过了，else语句生效了')
```
### 猜数字游戏
```python
#我的设计，着想了，过于想使用学过的知识，应该是怎么方便怎么设计
a = 24
while True:
    b = int(input('请输入一个整数：'))
    if a > b:
        print('你猜的数字小了')
        continue
    if a < b:
        print('你猜的数字大了')
        continue
    if a == b:
        break
else:
    print('bingo，答对了')
```

```python
#老师的设计
num1 = 24
while True:
    num2 = int(input('请输入一个数：'))
    if num1 > num2:
        print('太小了')
    elif num1 < num2:
        print('太大了')
    else:
        break
print('猜对了')
```

## 3、函数

> 尽量避免写重复的代码，少复制粘贴，也就是所谓的DRY原则——Don't Repeat Yourself。

> 函数：“喂”给函数一些数据，它就能内部消化，执行相应的功能，最终给你“吐”出你想要的东西

### 定义函数
```python
def 变量（参数）：
    函数体
    return 语句
```

```python
# 函数名：
# 1. 名字最好能体现函数的功能，一般用小写字母和单下划线、数字等组合
# 2. 不可与内置函数重名（内置函数不需要定义即可直接使用）
def math(x):
# 参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同
# 规范：括号是英文括号，后面的冒号不能丢
    y = 3*x + 5
# 函数体：函数的执行过程，体现函数功能的语句，要缩进，一般是四个空格
    return y
# return语句：后面可以接多种数据类型，如果函数不需要返回值的话，可以省略
```

### 调用函数
```python
a = math(10)
print(a)
```

### 参数类型

> 位置参数：按照对应参数的位置顺序传递数据
> 默认参数：直接在定义函数的时候给参数赋值，默认参数必须放在位置参数之后，默认参数可以改变
> 不定长参数：传递给参数的数量是可选的、不确定的，格式比较特殊，是一个星号*加上参数名，它的返回值也比较特殊，是一个元组
```python
def menu(*barbeque): # 带*号为不定长参数
    return barbeque
order = menu('烤鸡翅','烤茄子','烤玉米')
# 括号里的这几个值都会传递给参数barbeque
print(order)
print(type(order))
# >>> ('烤鸡翅', '烤茄子', '烤玉米')
# >>> <class 'tuple'>
```

### 返回多个值
```python
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
# >>> ('凉拌三丝', '溏心蛋')
# >>> <class 'tuple'> # 返回值为元组
```

### 变量作用域
```python
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
```

### 函数嵌套
```python
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
```

### 练习1
```python
# 返回字符串的长度

def str_len(x): 
    j = 0 # 1. 设置一个初始为0的计数器
    for i in x:
        j += 1 # 2.遍历字符串，每遍历一次，计数器加一
    return j # 3.返回计数器的值
    print(j)
str_len('三根皮带，四斤大豆')
```

### 练习2
```python
# 计算工资

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
```

### 练习3
```python
# 将下列代码用函数封装

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
```

```python
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
```

## 4、类与面向对象编程

> 类是某个特定的群体，实例是群体中某个具体的个体

> 对象等于类和实例的集合：即类可以看作是对象，实例也可以看作是对象

### 类的创建和调用
```python
# 类的属性what：是什么；类的方法how：怎么做
class Computer: # 类的创建，class+类名+冒号，后面语句缩进；类名的首字母必须大写
    screen = True # 类的属性用赋值语句
    def start(self): # 类的方法用函数语句：def+方法名(self)；与函数的不同点是必须在首位放置参数self
        print('电脑正在开机中') # 方法的具体执行过程
my_computer = Computer() # 实例名 = 类名()，类的实例化：在该类下创建一个具体的实例
print(my_computer.screen) # 属性和方法：要用句点.调用：实例名.属性名
my_computer.start() # 属性和方法：要用句点.调用：实例名.方法名()
```

### self的用处
```python
# 在定义时不能丢，在调用时要忽略
# self的作用相当于先给实例占了个位置，等到实例创建好就“功成身退，退位让贤”
# 在类的方法内部调用类的属性：self.属性名
# 在类的方法内部调用类的方法：self.方法名
# 效果类似于“变量作用域”：global
class Chinese:
    name = '小兔子'  # 类属性name
    def say(person):     
        print(person.name + '是中国人') # 如果想在类的内部调用类的属性，而实例又还没创建之前，我们就需要有个变量先代替实例接收数据，这个变量就是参数self。写法是实例名.属性，即self.属性
atm = Chinese()   # 创建Chinese的实例person
atm.say()         # 调用实例方法
class Chinese:
    def greeting(self):
        print('很高兴遇见你')
    def say(self):
        self.greeting() # 如果想在类的内部调用类的方法，也需要用到self来代表实例。
        print('我来自中国')
person = Chinese() # 创建实例person
person.say() # 调用say()方法
```

### 初始化方法——（属性）自动获得，（方法）随时调用
```python
# __new__ 构造函数：当每个实例对象创建时，该方法内的代码无须调用就会自动运行

class Chinese:
    def __init__(self): # __init__初始化方法，一种特殊的构造函数
        print('很高兴遇见你')
person = Chinese()
class Chinese:
    def __init__(self, name, birth, region): # 为类属性设置初始值，让类中的其他方法可以随时调用
        self.name = name   # self.name = '小兔子' 
        self.birth = birth  # self.birth = '湖南'
        self.region = region  # self.region = '广东'
    def born(self):
        print(self.name + '出生在' + self.birth)
    def live(self):
        print(self.name + '居住在' + self.region)    
person = Chinese('小兔子','湖南','广东') # 传入初始化方法的参数
person.born()
person.live()
```

### 类的标准化用例
```python
class Chinese:  # 类的创建
    eye = 'black'  # 类属性的创建
    def __init__(self,hometown):  # 类的初始化方法
        self.hometown = hometown  # 实例属性的创建
        print('程序持续更新中……')  # 初始化中的语句
    def born(self):  # 实例方法的创建
        print('我生在%s。'%(self.hometown))  # 方法的具体语句
xiaotuzi = Chinese('广东')  # 类的实例化
print(xiaotuzi.eye)  # 打印实例的属性（从类传递的）
xiaotuzi.born()  # 实例方法的调用
```

### 类的判断 isinstance()，用法类似于type()判断数据类型
```python
print(isinstance(1,int)) # 判断1是否为整数类的实例
print(isinstance(1,str))
print(isinstance(1,(int,str))) # 判断实例是否属于元组里几个类中的一个
```

### 类的继承
```python
# 以我为主，为我所用：定制以继承为前提，可创建新的属性和方法，可修改继承的属性和方法
# 继承的标准化用例
class Chinese: # class Chinese:在运行时相当于class Chinese(object):。而object，是所有类的父类，我们将其称为根类（可理解为类的始祖）
    eye = 'black'
    def eat(self):
        print('吃饭，选择用筷子。')
class Cantonese(Chinese):  # 通过继承，Chinese类有的，Cantonese类也有
    pass # 验证子类可以继承父类的属性和方法，进而传递给子类创建的实例
yewen = Cantonese()  # 子类创建的实例，从子类那间接得到了父类的所有属性和方法
print(yewen.eye)  # 子类创建的实例，可调用父类的属性
yewen.eat()  # 子类创建的实例，可调用父类的方法
```

#### 类的多层继承——深度拓展，子类创建实例可以调用父类所有属性和方法
```python
class Earthman:
    eye_number = 2 # 中国人继承了地球人
class Chinese(Earthman):
    eye_color = 'black' # 广东人继承了中国人，同时也继承了地球人。
class Cantonese(Chinese):
    pass
yewen = Cantonese() # 子类创建的实例可调用所有层级父类的属性和方法
print(yewen.eye_number)
print(yewen.eye_color)
```

#### 类的多重继承——宽度拓展，子类创建实例优先调用靠左父类的属性和方法
```python
# 就近原则：越靠近子类（即越靠左）的父类，越亲近，越优先考虑。子类调用属性和方法时，会先在靠左的父类里找，找不到才往右找。
class Su:
    born_city = 'Jiangsu'
    wearing = 'thick'
    def diet(self):
        print('我们爱吃甜。')
class Yue:
    settle_city = 'Guangdong'
    wearing = 'thin'
    def diet(self):
        print('我们吃得清淡。')
class Yuesu(Yue,Su):  
    pass
xiaoming = Yuesu() # 先在 Yue类找，找到了，打印出来。
print(xiaoming.wearing) # Yue类没有born_city，才去Su类找。
print(xiaoming.born_city) # 方法调用，和属性调用一样，也符合就近原则。
xiaoming.diet()
```

```python
# 一个简单的小例子
class C0:
    name = 'C0'
class C1:
    num = 1
class C2(C0):
    num = 2
class C3:
    name = 'C3'
class C4(C1,C2,C3):
    pass
c4 = C4()
print(c4.name) # 多重继承中，若某父类还有父类的话，会先继续往上找到顶。
print(c4.num)
```

### 类的定制——定制有两种：新增和重写
```python
class Chinese:
    def __init__(self, greeting = '你好', place = '中国'):
        self.greeting = greeting
        self.place = place
    def greet(self):
        print('%s！欢迎来到%s。' % (self.greeting, self.place))
class Cantonese(Chinese):
    def __init__(self, greeting = '雷猴', place = '广东'): # 通过参数的调整完成定制
        Chinese.__init__(self, greeting, place) # def语句后接父类.方法（参数）
yewen = Cantonese()
yewen.greet()
```

```python
# 一个简单的小例子
class Student:
    def __init__(self, name, job=None, time=0.00, time_effective=0.00): 
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective
    def count_time(self, hour, rate):
        self.time += hour
        self.time_effective += hour * rate
class Programmer(Student):
    def __init__(self, name, job=None, time=0.00, time_effective=0.00): 
        Student.__init__(self, name, job='programmer', time=0.00, time_effective=0.00)
    def count_time(Student,hour,rate):
        Student.time += hour
        Student.time_effective += hour * rate
student1 = Student('韩梅梅')
student2 = Programmer('李雷')
print(student1.job)
print(student2.job)
student1.count_time(10,0.8)
student2.count_time(10,1)
print(student1.time_effective)
print(student2.time_effective)
```

### 面向对象编程

> 用类编写程序一个直观的好处就是参数的传递会比普通函数要省事很多，也不必考虑全局变量和局部变量，因为类中的方法可以直接调用属性。

> 当项目难度越大，需要的参数越多，用类编写在程序的可拓展性、可读性、维护成本都会更胜一筹。

> 这就是面向对象编程：以对象为中心，将计算机程序看作一组对象的集合。

> 和函数类似，面向对象编程实际上也是一种对代码的封装。只不过，类能封装更多的东西，既能包含操作数据的方法，又能包含数据本身。所以，代码的可复用性也更高。

> 对于需要长期更新的代码而言，面向对象编程写成的代码结构会更清晰。代码的可读性、可拓展性和可维护性这几个方面都会优于面向过程编程。

## 5、项目实操

### 项目实操步骤
> 分析：明确项目目标

> 拆解（将一个问题拆解为多个步骤或者多种不同的层次，逐步解决和执行并最终达到效果）--分析过程拆到无法拆解为止

> 解决：代码实现，逐步执行

#### 三局两胜制小游戏
```python
# 敌我两PK，三局两胜制，用“计分板”判断最终胜利

from curses import keyname
from http import server
import random
from time import time, time_ns
from tkinter import Menu

player_victor = 0
enemy_victor = 0

for i in range(3):
    player_hp = random.randint(100,150) # 标准的变量名最好是用英文来表达含义，如果是多个单词组成，需要用英文下划线_来隔开。
    player_at = random.randint(30,50)
    enemy_hp = random.randint(100,150) # 标准的变量名最好是用英文来表达含义，如果是多个单词组成，需要用英文下划线_来隔开。
    enemy_at = random.randint(30,50)
    print('【玩家】血量 %d ，攻击力 %d' % (player_hp,player_at)) # 实现不同数据类型的拼接（不需要转换），用【格式化字符串】。 %s 字符串占位 ； %d 整数占位 ； %f 浮点数占位
    print('【敌人】血量 {} ，攻击力 {}' .format(enemy_hp,enemy_at)) # 更便捷，不担心用错类型，可指定位置，还可以传参数

    while (player_hp >= 0) and (enemy_hp >=0 ):
        player_hp = player_hp - enemy_at
        enemy_hp = enemy_hp - player_at
        print(player_hp)
        print(enemy_hp)

    if player_hp > enemy_hp:
        player_victor += 1 # 小技巧：player_victor = player_victor + 1，总是这样写有点烦人，我们可以写作player_victor += 1，这两个代码是等价的，都代表"如果if后的条件满足，变量就+1"。
        print('玩家胜利')
    elif player_hp < enemy_hp:
        enemy_victor += 1
        print('敌人胜利')
    else:
        print('你们打平了')

if player_victor > enemy_victor:
    print('玩家获得了最终胜利')
elif player_victor < enemy_victor:
    print('敌人获得了最终胜利')
else:
    print('你们打平了')
```

#### 人力/工时计算器
```python
# 我的设计：这个循环问题还是没解决
# key值判断法可以解决不在循环内用“循环”的问题
# import math
# key = 1
# def estimated(size=1,number=None,time=None):
#     if (number == None) and (time != None):
#         number = math.ceil(size * 80 / time)
#         print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))  
#     elif (number != None) and (time == None):
#         time = size * 80 / number
#         print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))
# def again():
#     global key # 哪里需要用，哪里声明全局变量
#     contour = input('请确认是否继续计算，输入y-继续，输入其他则退出程序')
#     if contour == 'y':
#         key = 0
# def main():
#     if key == 1:
#         types = int(input('请选择计算类型：（1-人力计算，2-工时计算）'))
#         size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
#         while True:
#             if types == 1:
#                 time = float(input('请输入工时数量：（请输入小数）'))
#                 return estimated(size,time),again()
#             elif types == 2:
#                 number = int(input('请输入人力数量：（请输入整数）'))
#                 return estimated(size,number),again()
# main()
```

```python
# 老师的设计：采用面向对象编程的思维
# 面向对象编程——考虑先创建某个类，在类中设定好属性和方法，即是什么，和能做什么；再以类为模版创建一个实例对象，用这个实例去调用类中定义好的属性和方法即可
import math
class Project:
    def __init__(self):
        self.key = 1
    def input(self):
        choice = input('请选择计算类型：（1-工时计算，2-人力计算）')
        if choice == '1':
            self.size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
            self.number = int(input('请输入人力数量：（请输入整数）'))
            self.time = None
        if choice == '2':
            self.size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
            self.number = None
            self.time = float(input('请输入工时数量：（请输入小数）'))
    def estimated(self):
        # 人力计算
        if (self.number == None) and (self.time != None):
            self.number = math.ceil(self.size * 80 / self.time)
            print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(self.size,self.time,self.number)) 
        # 工时计算
        elif (self.number != None) and (self.time == None):
            self.time = self.size * 80 / self.number
            print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(self.size,self.number,self.time))  
    def again(self):
        a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
        if a != 'y':
            # 如果用户不输入'y'，则把key赋值为0
            self.key = 0  
    # 主函数
    def main(self):
        print('欢迎使用工作量计算小程序！')
        while self.key == 1:
            self.input()
            self.estimated()
            self.again()
        print('感谢使用工作量计算小程序！')
# 创建实例
project1 = Project()
project1.main()
# 面向过程编程——考虑程序具体的执行过程（即先做什么后做什么）
import math
# 变量key代表循环运行程序的开关
key = 1
# 采集信息的函数
def myinput():
    choice = input('请选择计算类型：（1-工时计算，2-人力计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None
        return size,number,time
        # 这里返回的数据是一个元组
    if choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        time = float(input('请输入工时数量：（请输入小数）'))
        return size,number,time
        # 这里返回的是一个元组
# 完成计算的函数
def estimated(my_input):
    # 把元组中的数据取出来
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    # 人力计算
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number)) 
    # 工时计算
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  
# 询问是否继续的函数
def again():
    # 声明全局变量key，以便修改该变量
    global key
    a = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
    if a != 'y':
        # 如果用户不输入'y'，则把key赋值为0
        key = 0  
# 主函数
def main():
    print('欢迎使用工作量计算小程序！')
    while key == 1:
        my_input = myinput()
        estimated(my_input)
        again()
    print('感谢使用工作量计算小程序！')
main()
```

#### 与机器人猜拳
```python
import random
# 出拳
punches = ['石头','剪刀','布']
computer_choice = random.choice(punches)
user_choice = ''
user_choice = input('请出拳：（石头、剪刀、布）')  # 请用户输入选择
while user_choice not in punches:  # 当用户输入错误，提示错误，重新输入
    print('输入有误，请重新出拳')
    user_choice = input()
# 亮拳
print('————战斗过程————')
print('电脑出了：%s' % computer_choice)
print('你出了：%s' % user_choice)
# 胜负
print('—————结果—————')
if user_choice == computer_choice:  # 使用if进行条件判断
    print('平局！')
# 电脑的选择有3种，索引位置分别是：0石头、1剪刀、2布。
# 假设在电脑索引位置上减1，对应：-1布，0石头，1剪刀，皆胜。
elif user_choice == punches[punches.index(computer_choice)-1]:
    print('你赢了！')
else:
    print('你输了！')
```

### 完整项目实操：图书馆管理系统

> 我的思路
> 第一步：对象为图书馆Lib，子类为书
> 第二步：图书馆属性，用元祖存放书和在借在还状态；图书馆方法，用key=0/1来判断借还装填
> 第三步：书的属性，index来获取书的名字/状态；书的方法1，key +- 1来确定借还；书的犯法2，index来查询/添加图书
> 第四步：实例化完成调用

> 老师的思路
> 处理对象是每本具体的书，而每本书都有自己的属性信息，所以我们可以定义一个Book类，利用Book类创建一个个书的实例，绑定属性
> 管理系统的运行主体，是多个可供选择的功能的叠加，所以我们可以创建一个系统运行类BookManager，将查询书籍、添加书籍等功能封装成类中的方法以供调用
> 为了让类的结构更清晰，我们可以将这个选择菜单也封装成一个方法menu()，方便调用其他方法

```python
class Book:
    def __init__(self,bookname,author,recommended,status=0): # 利用初始化方法__init__，让实例被创建时自动获得这些属性
        self.bookname = bookname
        self.author = author
        self.recommended = recommended
        self.status = status # 给status设置默认值，0表示未借出，1表示已借出
    # def show_info(self):
    def __str__(self): # Python中方法名形式左右带双下划线的为特殊方法
    # __str__打印对象即可打印出该方法中的返回值，而无须再调用方法
        if self.status == 0: # 相当于函数中的global变量，self可以提供占位，并在当前类中调用其他属性和方法
            state = '未借出'  # 此处应该单独设置一个变量接收“状态”，分清楚变量的作用范围，也就是要理解计算机的理解逻辑
        else:
            state = '已借出'
        return '名称：{} 作者：{} 推荐语：{} 状态：{}'.format(self.bookname,self.author,self.recommended,state) # 此处为类中修改属性，传入的参数名应该与修改的参数名一致
# book1 = Book('像自由一样美丽', '林达', '你要用光明来定义黑暗，用黑暗来定义光明') # 传入参数，创建实例
# print(book1) # 此处的类实例化是为了测试代码是否有bug

# 创建一个FictionBook的子类，给书本加入类型数据
class FictionBook(Book): # 子类继承父类，需要指定父类名啊，这点怎么能忘记
    def __init__(self,bookname,author,recommended,status=0,type = '虚构类'):
        Book. __init__(self,bookname,author,recommended,status=0) # 继承Book的构造属性
        self.type = type # 添加子类独有的属性

    def __str__(self):
        state = '未借出'
        if self.status == 1:
            state = '已借出'
        return '类型：{} 名称：{} 作者：{} 推荐语：{} 状态：{}'.format(self.type,self.bookname,self.author,self.recommended,state)

FictionBook1 = FictionBook('囚鸟','冯内古特','我们都是受困于时代的囚鸟')
print(FictionBook1)
```

```python
# 我的设计，没有注意方法之间的调用关系
# class BookManager():
#     def memu(self):
#         self.menu = int(input('请输入对应数字选择功能：1.查询所有书籍；2.添加书籍；3.借阅书籍；4.归还书籍；5.退出系统')) # 数字控制流程
# book1 = BookManager()
# print(book1)
```

```python
# 老师的设计，注重程序内部调用的逻辑
class BookManager:
    book = [] # 创建一个列表，列表里每个元素都是Book类的一个实例
    def __init__(self): # 构造函数，对象实例化，无需调用自动运行
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)

        # self.book.append.book1 # 往列表依次添加元素，注意调用类属性book时，self不能丢
        self.book.append(book1)
        # self.book.append.book2 # 提示错误：AttributeError: 'builtin_function_or_method' object has no attribute 'book1'
        self.book.append(book2)
        # self.book.append.book3 # 因为对象属性没有被传输进去，append()方法调用错误，追加列表元素是方法不是属性
        self.book.append(book3)

        # self.book = [book1,book2,book3]
        # 以上3行代码可以简化为一行，不需要在前面创建空列表接收数据

    def menu(self):
        choice = int(input('请输入对应数字选择功能：1.查询所有书籍；2.添加书籍；3.借阅书籍；4.归还书籍；5.退出系统'))
        while True:
            if choice == 1:
                self.show_all() # 调用对象方法时self不能忘
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            else:
                # quick_sys() # 当你设计方法时，先想想这个方法的内部逻辑是否可完成
                break # 老师这里直接用break结束循环，表示退出系统，言简意赅

    def show_all(self):
        for i in self.book: # 遍历实例里的每个元素
            print(i) # 列表book里的每个元素都是基于Book类创建的实例对象，所以每个元素会自动拥有Book类的方法__str__：直接打印返回值

    def add_book(self):
        new_bookname = input('请输入书籍名字：') # 定义的新的变量名，在之后需要调用才会有效
        new_author = input('请输入作者名称：')
        new_recommended = input('请输入推荐语：')
        new_status = int(input('请输入借出状态。0表示未借出，1表示已借出：'))
        new_book = Book(new_bookname,new_author,new_recommended,new_status) # 调用Book类，传入新书的参数
        self.book.append(new_book) # 将新书追加到列表末尾
        print('新书录入成功')
        # self.new_bookname = new_bookname # 这里是错误的做法，只是将新书的属性又赋值了一遍，没有追加到列表里面
        # self.new_author = new_author
        # self.new_recommended = new_recommended
        # self.new_status = new_status

    def lend_book(self):
        borrow_bookname = input('请输入你想借走的书籍名称：')
        res = self.check_bookname(borrow_bookname) # 将检查书名的其中一个属性赋值给 res
        # 借书的时候要检查有没有这个书名
        for book in self.book:
            if res != None: # 漏掉了 .bookname ，属性值与属性值才能比较；列表不能与str比较
                if res.status == 1: # res 自动获得了后面的书本其他的属性；这就是构造函数的意义：属性自动获得，方法随时调用
                    print('本书已经被人借走了哦')
                    break
                else:
                    res.status = 1
                    print('本书已经成功被你借到了哦')
                    break
            else:
                continue
        else:
            print('图书馆里没有这本书哦')

    def return_book(self):
        return_bookname = input('请输入您还书的名称：')
        # 还书的时候也要检查有没有这个书名
        res = self.check_bookname(return_bookname)
        if res == None:
            print('我们没有这本书哦')
        else:
            if res.status == 0:
                print('已经被借出了哦，你是不是还错书了')
            else:
                print('谢谢，已经收到您还的书了')
                res.status = 0

    # def check_bookname(self,checkname): 
        # 封装一个函数检查有没有这个书名，不用重复写代码
    def check_bookname(self,bookname):
        # 为什么要用bookname，因为需要与前面定义的变量名保持一致，也就是不用传入全部参数，也可以获得后面的推荐语、借出状态等其他属性
        for book in self.book: # 遍历每个Book实例
            if book.bookname == bookname: # 遇到实例名与输入书籍名一致
                return book # 返回该实例对象，遇到return语句方法停止执行
        else:
            return None # 若没有这本书，返回 None 值
BookManager1 = BookManager() # 对象实例化
BookManager1.menu()
```

```python
# 封装一个函数检查有没有这个作者名

# 我的设计，考虑获取列表中的值来比较，但是值有很多种不同的，需要传入其他的列表来比较
# def check_author(self,bookauthor):
#     for author in self.author:
#         if  book.author == bookauthor:
#             retrun book
#     else:
#         return None
```

```python
# 老师的设计
class Book:
    def __init__(self,bookname,author,recommended,status=0): # 利用初始化方法__init__，让实例被创建时自动获得这些属性
        self.bookname = bookname
        self.author = author
        self.recommended = recommended
        self.status = status # 给status设置默认值，0表示未借出，1表示已借出
    # def show_info(self):
    def __str__(self): # Python中方法名形式左右带双下划线的为特殊方法
    # __str__打印对象即可打印出该方法中的返回值，而无须再调用方法
        if self.status == 0: # 相当于函数中的global变量，self可以提供占位，并在当前类中调用其他属性和方法
            state = '未借出'  # 此处应该单独设置一个变量接收“状态”，分清楚变量的作用范围，也就是要理解计算机的理解逻辑
        else:
            state = '已借出'
        return '名称：{} 作者：{} 推荐语：{} 状态：{}'.format(self.bookname,self.author,self.recommended,state) # 此处为类中修改属性，传入的参数名应该与修改的参数名一致
# book1 = Book('像自由一样美丽', '林达', '你要用光明来定义黑暗，用黑暗来定义光明') # 传入参数，创建实例
# print(book1) # 此处的类实例化是为了测试代码是否有bug
class AuthorManager:
    authors = []
    # 创建一个存放作者名的列表
    def __init__(self):
        book1 = Book('撒哈拉的故事','三毛','我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book2 = Book('梦里花落知多少','三毛','人人都曾拥有荷西，虽然他终会离去。')
        book3 = Book('月亮与六便士','毛姆','满地都是六便士，他却抬头看见了月亮。')
        self.books = [book1,book2,book3]
        # 将三个实例放在列表books里
        self.authors.append(book1.author)
        self.authors.append(book2.author)
        self.authors.append(book3.author)
        # 将三个实例的作者名添加到列表author里
     
    def authormenu(self):
        while True:
            print('1.查询书籍')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_author_book()
                # 调用方法
            else:
                print('感谢使用！')
                break
     
    def show_author_book(self):
        author = input('你想找谁的书呢？')
        if author in self.authors:
            for book in self.books:
                if book.author == author:
                    print(book)
        else:
            print('很可惜，我们暂时没有收录这位作者的作品')

AuthorManager1 = AuthorManager() # 对象实例化
AuthorManager1.authormenu()
```

### 发邮件
```python
import smtplib # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText # email 用于构建邮件内容
from email.header import Header
from_addr = input('请输入发件邮箱：') # 发信方的信息：发信邮箱，授权码
password = input('请输入发件邮箱密码：')
to_addr = input('请输入收件邮箱：') # 收信方邮箱
smtp_server = 'smtp.exmail.qq.com' # 发信服务器
mailtext ='''
123
456
789
'''
msg = MIMEText(mailtext,'plain','utf-8') # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg['From'] = Header(from_addr) # 邮件头信息
msg['To'] = Header(to_addr) # 必须放在邮件内容之后，因为msg需先定义才能使用
msg['Subject'] = Header('python test')
server = smtplib.SMTP_SSL(smtp_server) # 报错：smtplib.SMTPServerDisconnected: please run connect() first 3.7之后改版，需在在括号内加入host参数
server.connect(smtp_server,465)
server.login(from_addr, password) # 登录发信邮箱
server.sendmail(from_addr, to_addr, msg.as_string()) # 发送邮件
server.quit() # 关闭服务器
```

### 群发邮件
```python
import smtplib # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText # email 用于构建邮件内容
from email.header import Header # 用于构建邮件头
import csv # 引用csv模块，用于读取邮箱信息
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')
smtp_server = 'smtp.exmail.qq.com' # 发信服务器
text='''
123
456
789
'''
data = [['123 ', '123@qq.com'],['456', '456@qq.com']] # 待写入csv文件的收件人数据：人名+邮箱
with open('to_addrs.csv', 'w', newline='') as f: # 写入收件人数据
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
with open('to_addrs.csv', 'r') as f: # 读取收件人数据，并启动写信和发信流程
    reader = csv.reader(f)
    for row in reader: 
        to_addrs=row[1]
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server,465)
        server.login(from_addr, password)
        try:
            server.sendmail(from_addr, to_addrs, msg.as_string())
            print('恭喜，发送成功')
        except:
            print('发送失败，请重试')
server.quit() # 关闭服务器
```

### 制作二维码
```python
from MyQR import myqr
myqr.run(
    words='http://www.51biaoshi.com',
    # 扫描二维码后，显示的内容，或是跳转的链接
    version=5,  # 设置容错率
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture='C:\\1.png',  # 图片所在目录，可以是动图
    colorized=True,  # 黑白(False)还是彩色(True)
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。默认为1.0。
    brightness=1.0,  # 用来调节图片的亮度，用法同上。
    save_name='C:\\2.png',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    )
```

### 求绝对值的三种方法
```python
import math
def abs_value1(): # 方法1：条件判断
    a = float(input('1.请输入一个数字：'))
    if a >= 0:
        a = a
    else:
        a = -a
    print('绝对值为：%f' % a)
def abs_value2(): # 方法2：内置函数 abs()
    a = float(input('2.请输入一个数字：'))
    a = abs(a)
    print('绝对值为：%f' % a)
def abs_value3(): # 方法3：内置模块 math
    a = float(input('3.请输入一个数字：'))
    a = math.fabs(a)
    print('绝对值为：%f' % a)
abs_value1()
abs_value2()
abs_value3()
```

### 录入楼栋信息
```python
import csv
#调用csv模块
with open('assets.csv', 'a', newline='') as csvfile:
#调用open()函数打开csv文件，传入参数：文件名“assets.csv”、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header=['小区名称', '地址', '建筑年份', '楼栋', '单元', '户室', '朝向', '面积']
    writer.writerow(header)

title=input('请输入小区名称：')
address = input('请输入小区地址：')
year = input('请输入小区建造年份：')
block = input('请输入楼栋号：')


unit_loop = True
while unit_loop:
    unit=input('请输入单元号：')
    start_floor = input('请输入起始楼层：')
    end_floor = input('请输入终止楼层：')

    # 开始输入模板数据
    input('接下来请输入起始层每个房间的门牌号、南北朝向及面积，按任意键继续')
    
    start_floor_rooms = {}
    floor_last_number = []
    # 收集起始层的房间信息
    
    # 定义循环控制量
    room_loop = True
    while room_loop:
        last_number = input('请输入起始楼层户室的尾号:（如01，02）')
        floor_last_number.append(last_number)
        #将尾号用append()添加列表里，如floor_last_number = ['01','02']
        room_number = int(start_floor + last_number)
        #户室号为room_number,由楼层start_floor和尾号last_number组成,如301
    
        direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number ))
        area = int(input('请输入 %d 的面积，单位 ㎡ ：' % room_number))
        start_floor_rooms[room_number] = [direction,area]
        # 户室号为键，朝向和面积组成的列表为值，添加到字典里，如start_floor_rooms = {301:[1,70]}
    
        continued= input('是否需要输入下一个尾号？按 n 停止输入，按其他任意键继续：')
        #加入打破循环的条件
        if continued == 'n':
            room_loop = False
        else:
            room_loop = True       
    
    unit_rooms = {}
    #新建一个放单元所有户室数据的字典
    unit_rooms[start_floor] = start_floor_rooms
    #unit_rooms={3:{301:[1,80],302:[1,80],303:[2,90],304:[2,90]}}
    for floor in range(int(start_floor) + 1, int(end_floor) + 1):
    #遍历除初始楼层外的其他楼层
        floor_rooms = {}
        #每个楼层都建立一个字典
        for i in range(len(start_floor_rooms)):
        #遍历每层有多少个房间，这里是3，即执行for i in range 3 的循环
            number = str(floor) + floor_last_number[i]
            info = start_floor_rooms[int(start_floor + floor_last_number[i])]
            # 依次取出字典start_floor_rooms键对应的值，即面积和朝向组成的列表
            floor_rooms[int(number)] = info
            #给字典floor_rooms添加键值对，floor_rooms = {401:[1,80]}
        unit_rooms[floor] = floor_rooms
    
    with open('assets.csv', 'a', newline='')as csvfile:
    #Mac用户要加多一个参数 encoding = 'GBK'
        writer = csv.writer(csvfile, dialect='excel')
        for sub_dict in unit_rooms.values():
            for room,info in sub_dict.items():
                dire = ['', '南北', '东西']
                writer.writerow([title,address,year,block,unit,room,dire[info[0]],info[1]])   
    
    unit_continue = input('是否需要输入下一个单元？按 n 停止单元输入，按其他任意键继续：')
    if unit_continue == 'n':
        unit_loop = False
    else:
        unit_loop = True

print('恭喜你，资产录入工作完成！')  
```

## 6、学习思维

### 高效学习
```python
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
```

```python
# 老师的做法，总是感觉更智能
for i in range(1,10):
    for j in range(1,i+1):
        print('{} * {} = {}'.format(i,j,i*j),end = ' ')
    print('')
```

```python
# 合并两班成绩并排序，涉及到新知识需要用百度查询大法，一步步验证、排查并直到得出结果
a = [91, 95, 97, 99]
b = [92, 93, 96, 98]
a.extend(b)
a = sorted(a)
print(a)
```
```pyton
# 学完库的知识再来补齐的我做法
# 计算平均分，低于平均分打印出来
from numpy import *
a = [91, 95, 97, 99]
b = [92, 93, 96, 98]
a_avg = mean(a)
b_avg = mean(b)
print('{} , {}'.format(a_avg,b_avg))
```

### 代码报错
```python
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
```

### 构思产品
1. 积累生活经验
2. 提出产品需求
	- 替代重复性劳动
	- 制作工具解决问题
3. 形成技术方案
	- 分析问题，明确结果
	- 思考需要的知识，或学习新知识
	- 思考切入点
	- 尝试解决问题的一部分
	- 重复以上步骤
4. 完成程序代码

#### 当我吃午饭时，我在吃些什么
```python
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
```

```python
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
```

#### 滚动的广告牌
```python
import os, time
def main():  # 用函数封装，可复用性会高一些（可在其他的.py文件里调用该函数。）
    content = ' 1234567890 '  # 广告词可自定义。
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
```

## 7、文件操作

### 编码与解码
```python
# 编码 .encode() 本质就是把str（字符串）类型的数据，利用不同的编码表，转换成bytes（字节）类型的数据
# 解码 .decode()
print('小兔子'.encode('utf-8'))
print('小兔子'.encode('gbk'))
print(b'\xe5\xb0\x8f\xe5\x85\x94\xe5\xad\x90'.decode('utf-8')) # 字母b表示其为字节（byte）类型的数据
print(b'\xd0\xa1\xcd\xc3\xd7\xd3'.decode('gbk')) # \x是分隔符，用来分隔一个字节和另一个字节
print(type('小兔子')) # 字符串类型
print(type(b'\xe5\xb0\x8f\xe5\x85\x94\xe5\xad\x90')) # 字节类型
# https://www.baidu.com/s?wd=%E5%90%B4%E6%9E%AB 其中的%，它们也是分隔符
# \xe5\x90\xb4\xe6\x9e\xab  # Python编码“吴枫”的结果
# %E5%90%B4%E6%9E%AB # 网址里的“吴枫”
```

### 文件读取
```python
# 分三步：开——读——关

# 如果你要打开的文件和open.py在同一个文件夹里，使用相对路径就行了，而要使用其他文件夹的文件则需使用绝对路径
# Windows系统里，用\来表示绝对路径，/来表示相对路径，\在Python中是转义字符，所以时常会有冲突。为了避坑，Windows的绝对路径通常要稍作处理，写成以下两种格式:
open('C:\\Users\\Ted\\Desktop\\test\\abc.txt')
#将'\'替换成'\\'
open(r'C:\Users\Ted\Desktop\test\abc.txt')
#在路径前加上字母r
file1 = open(r'D:\OneDrive\GitHub\SquidGame\outputfile.txt','r',encoding='utf-8') # 开
# 第一个参数：文件路径；第二个参数：r表示read；第三个参数：返回数据的编码
filecontent = file1.read() # 存
print(filecontent) # 读
file1.close() # 关
```

### 文件写入
```python
# 分三步：开——写——关

# 在'w'和'a'模式下，如果你打开的文件不存在，那么open()函数会自动帮你创建一个
# file1 = open(r'D:\OneDrive\GitHub\SquidGame\outputfile.txt','w',encoding='utf-8') # 开
# w模式会暴力清除所有数据；a模式会在末尾追加数据
f = open(r'D:\OneDrive\GitHub\SquidGame\outputfile.txt','a+',encoding='utf-8') # 开
# 使用a或者w模式会出现 io.UnsupportedOperation: not readable 错误，此时并没有真正的写入，而是还存在于内存中；需使用a+或者w+模式才能读取出来
f.write('包子\n') # 写
f.write('饺子\n') # \n表示写入换行
f.write('丸子\n')
file = f.read() # 存
print(file)
f.close() # 关
```

### 文件读写的几种方式
```python
# a+ 追加且可读，ab+ 二进制追加且可读
# w+ 读写，wb+ 二进制读写；以二进制的方式打开一个文件用于写入。因为图片和音频是以二进制的形式保存的，所以使用wb+模式就好
# r+ 读写，rb+ 二进制读写

# with open……as写法
with open(r'D:\OneDrive\GitHub\SquidGame\outputfile.txt','a+',encoding='utf-8') as file1:
    file1.write('小兔子\n')
    filecontent = file1.read()
print(filecontent)
# 使用with关键字的写法，意思是：用变量名打开文件
with open('abc.txt','a') as file1:
#with open('文件地址','读写模式') as 变量名:
    #格式：冒号不能丢
    file1.write('张无忌\n') 
    #格式：对文件的操作要缩进
    #格式：无需用close()关闭
```

### 打印每个学生的总成绩
```python
# 我的做法
with open('D:\OneDrive\GitHub\SquidGame\scores.txt','r',encoding='utf-8') as file:
    file_lines = file.readlines() # 方法调用记得加（），出现 TypeError: 'builtin_function_or_method' object is not iterable 错误，一般是括号忘记带了
for i in file_lines:
    data = i.split() # 按行读取，记得切分为列表
    sum = 0 #先把总成绩设为0
    for score in data[1:]: #遍历列表中第1个数据和之后的数据
        sum = int(score) + sum #然后依次加起来，但分数是字符串，所以要转换
    res = data[0] + str(sum) #结果就是学生姓名和总分
    print(res)
```

```python
# 老师的做法
file = open('D:\OneDrive\GitHub\SquidGame\scores.txt','r',encoding='utf-8') 
file_lines = file.readlines()
file.close()

final_scores = [] 

for i in file_lines:
    data =i.split()    
    sum = 0                    
    for score in data[1:]:     
        sum = sum + int(score)     
    result = data[0]+str(sum)+'\n'    
    final_scores.append(result)

winner = open('D:\OneDrive\GitHub\SquidGame\winner.txt','w',encoding='utf-8') 
winner.writelines(final_scores)
winner.close()
```

### 成绩从高到低排序
```python
# 下面注释掉的代码，皆为检验代码（验证每一步的思路和代码是否达到目标，可解除注释后运行）。

file1 = open('winner.txt','r',encoding='utf-8') 
file_lines = file1.readlines() 
file1.close()

dict_scores = {}
list_scores = []
final_scores = []

# print(file_lines) 
# print(len('\n'))

# 打印结果为：['罗恩102\n', '哈利383\n', '赫敏570\n', '马尔福275\n']
# 经过测试，发现'\n'的长度是1。所以，名字是“第0位-倒数第5位”，分数是“倒数第4位-倒数第二位”。
# 再根据“左取右不取”，可知：name-[:-4],score-[-4:-1]

for i in file_lines:  # i是字符串。
    print(i)
    name = i[:-4]  # 取出名字（注：字符串和列表一样，是通过偏移量来获取内部数据。）
    score = int(i[-4:-1])  # 取出成绩
    print(name)
    print(score)
    dict_scores[score] = name  # 将名字和成绩对应存为字典的键值对(注意：这里的成绩是键)
    list_scores.append(score)

# print(list_scores)
list_scores.sort(reverse=True)  # reverse，逆行，所以这时列表降序排列，分数从高到低。
# print(list_scores)

for i in list_scores:
    result = dict_scores[i] + str(i) + '\n'
    # print(result)
    final_scores.append(result)

print(final_scores)  # 最终结果

winner_new = open('winner_new.txt','w',encoding='utf-8') 
winner_new.writelines(final_scores)
winner_new.close()
```

### 复制图片
```python
with open('1.png','rb') as file1: # 奇怪的是用rb+模式写出来的图片打不开
    filecontent = file1.read()
with open('2.png','wb') as file2: # 奇怪的是用wb+模式写出来的图片打不开
    file2.write(filecontent)
```

### 古诗词填空
```python
list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']  # 将要默写的诗句放在列表里。
with open ('poem1.txt','r',encoding='utf-8') as f: # 字符串文本一定要记得编码：utf-8
    lines = f.readlines()
print(lines)
with open('poem2.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)
```

## 8、模块操作

```python
# 以下为test_mokuai模块的内容
sentence = '从前有座山，'
def mountain():
    print('山里有座庙，')
class Temple:
    sentence = '庙里有个老和尚，'
    def reading(self):
        print('在讲一个长长的故事。')
for i in range(10):
    print(sentence)
    mountain()
    A = Temple()
    print(A.sentence)
    A.reading()
    print()
```

### 导入模块，可同时导入多个文件
```python
# 模块文件命名：需要添加分割符号，最好使用下划线‘_’
import test_mokuai
# 导入模块后，要使用模块中的变量、函数、类，需要在使用时加上模块.的格式
print(test_mokuai.sentence) # 属性需要加打印语句才能在终端显示结果
test_mokuai.mountain() # 方法不需要打印语句因为定义时加了运行语句
A = test_mokuai.Temple()
# 实例化后，调用模块-类下面的方法不用加模块名，因为前面实例化的时候已经声明了模块
print(A.sentence)
A.reading()
```

### 导入模块重命名
```python
# import…as… 比如import test_mokuai太长，就可以用import test_mokuai as tm语句，意思是为“test_mokuai”取个别名为“tm”
import test_mokuai as tm
print(tm.sentence)
tm.mountain()
A = tm.Temple()
print(A.sentence)
A.reading()
```

### 导入模块中的指定部分，且可以直接使用，无需加上“模块.”前缀
```python
# from（模块名）import（指定模块中的变量名/函数名/类名）
# from（模块名）import * (*代表“模块中所有的变量、函数、类”)
from test_mokuai import Temple
A = Temple() # TypeError: Temple.reading() missing 1 required positional argument: 'self'——不实例化就会出现“类型错误”
A.sentence
A.reading()
```

### 借用别人的模块
```python
# 打开终端，Windows用户输入pip install + 模块名，点击enter即可
# 打开终端，苹果电脑输入：pip3 install + 模块名，点击enter即可
```

### 自学模块，将案例做成笔记，如下：
```python
import random  # 调用random模块
a = random.random()  # 随机从0-1之间（包括0不包括1）抽取一个小数
print(a)
a = random.randint(0,100)  # 随机从0-100（包括0和100）之间抽取一个数字
print(a)
a = random.choice('abcdefg')  # 随机从字符串，列表等对象中抽取一个元素（可能会重复）
print(a)
a = random.sample('abcdefg', 3) # 随机从字符串，列表等对象中抽取多个不重复的元素
print(a)
items = [1, 2, 3, 4, 5, 6]  # “随机洗牌”，比如打乱列表
random.shuffle(items)
print(items)

# 使用dir()函数查看一个模块，看看它里面有什么变量、函数、类、类方法
# 对于查到的结果"__xx__"结构的(如__doc__)，它们是系统相关的函数，我们不用理会，直接看全英文的函数名即可。
import random  # 调用random模块
print(dir(random))
```