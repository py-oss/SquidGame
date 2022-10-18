# 类是某个特定的群体，实例是群体中某个具体的个体
# 对象等于类和实例的集合：即类可以看作是对象，实例也可以看作是对象

# 类的创建和调用
# 类的属性what：是什么；类的方法how：怎么做
class Computer: # 类的创建，class+类名+冒号，后面语句缩进；类名的首字母必须大写
    screen = True # 类的属性用赋值语句
    def start(self): # 类的方法用函数语句：def+方法名(self)；与函数的不同点是必须在首位放置参数self
        print('电脑正在开机中') # 方法的具体执行过程
my_computer = Computer() # 实例名 = 类名()，类的实例化：在该类下创建一个具体的实例
print(my_computer.screen) # 属性和方法：要用句点.调用：实例名.属性名
my_computer.start() # 属性和方法：要用句点.调用：实例名.方法名()

# self的用处
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

# 初始化方法——（属性）自动获得，（方法）随时调用
# 构造函数：当每个实例对象创建时，该方法内的代码无须调用就会自动运行
class Chinese:
    def __init__(self): # 注意def后面空一格，可以看做一种特殊的写法
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

# 类的标准化用例
class Chinese:  # 类的创建
    eye = 'black'  # 类属性的创建
    def __init__(self,hometown):  # 类的初始化方法
        self.hometown = hometown  # 实例属性的创建
        print('程序持续更新中……')  # 初始化中的语句
    def born(self):  # 实例方法的创建
        print('我生在%s。'%(self.hometown))  # 方法的具体语句
wufeng = Chinese('广东')  # 类的实例化
print(wufeng.eye)  # 打印实例的属性（从类传递的）
wufeng.born()  # 实例方法的调用

# 类的继承和定制
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

# 类的判断 isinstance()，用法类似于type()判断数据类型
print(isinstance(1,int)) # 判断1是否为整数类的实例
print(isinstance(1,str))
print(isinstance(1,(int,str))) # 判断实例是否属于元组里几个类中的一个

# 类的多层继承——深度拓展，子类创建实例可以调用父类所有属性和方法
class Earthman:
    eye_number = 2 # 中国人继承了地球人
class Chinese(Earthman):
    eye_color = 'black' # 广东人继承了中国人，同时也继承了地球人。
class Cantonese(Chinese):
    pass
yewen = Cantonese() # 子类创建的实例可调用所有层级父类的属性和方法
print(yewen.eye_number)
print(yewen.eye_color)

# 类的多重继承——宽度拓展，子类创建实例优先调用靠左父类的属性和方法
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
# 一个例子
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

# 类的定制——定制有两种：新增和重写
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
# 一个例子
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

# 面向对象编程
# 用类编写程序一个直观的好处就是参数的传递会比普通函数要省事很多，也不必考虑全局变量和局部变量，因为类中的方法可以直接调用属性。
# 当项目难度越大，需要的参数越多，用类编写在程序的可拓展性、可读性、维护成本都会更胜一筹。
# 这就是面向对象编程：以对象为中心，将计算机程序看作一组对象的集合。
# 和函数类似，面向对象编程实际上也是一种对代码的封装。只不过，类能封装更多的东西，既能包含操作数据的方法，又能包含数据本身。所以，代码的可复用性也更高。
# 对于需要长期更新的代码而言，面向对象编程写成的代码结构会更清晰。代码的可读性、可拓展性和可维护性这几个方面都会优于面向过程编程。