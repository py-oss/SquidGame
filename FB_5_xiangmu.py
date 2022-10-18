# 分析 —— 拆解（将一个问题拆解为多个步骤或者多种不同的层次，逐步解决和执行并最终达到效果） —— 解决

# 拆到无法拆解为止

# 模块：是一个装着许多神奇函数的百宝箱，不过想要使用这个百宝箱里的函数，得先用 import 模块名 这样一句代码来打开它。

# “不懂就查”：百度，输入词条“Python 遇到的问题”

# 敌我两PK，三局两胜制，用“计分板”判断最终胜利
from curses import keyname
import random
from time import time, time_ns

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

# 人力/工时计算器 key值判断法可以解决不在循环内用“循环”的问题
### 这个循环问题还是没解决
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

### 练习1
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

# 明确项目目标
# 我的思路
# 第一步：对象为图书馆Lib，子类为书
# 第二步：图书馆属性，用元祖存放书和在借在还状态；图书馆方法，用key=0/1来判断借还装填
# 第三步：书的属性，index来获取书的名字/状态；书的方法1，key +- 1来确定借还；书的犯法2，index来查询/添加图书
# 第四步：实例化完成调用

# 分析过程，拆解项目
# 老师的思路
# 处理对象是每本具体的书，而每本书都有自己的属性信息，所以我们可以定义一个Book类，利用Book类创建一个个书的实例，绑定属性
# 管理系统的运行主体，是多个可供选择的功能的叠加，所以我们可以创建一个系统运行类BookManager，将查询书籍、添加书籍等功能封装成类中的方法以供调用
# 为了让类的结构更清晰，我们可以将这个选择菜单也封装成一个方法menu()，方便调用其他方法

# 代码实现，逐步执行
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

class BookManager(Book):