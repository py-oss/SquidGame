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