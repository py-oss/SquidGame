# 导入模块，可同时导入多个文件
# 模块文件命名：需要添加分割符号，最好使用下划线‘_’
import test_mokuai
# 导入模块后，要使用模块中的变量、函数、类，需要在使用时加上模块.的格式
print(test_mokuai.sentence) # 属性需要加打印语句才能在终端显示结果
test_mokuai.mountain() # 方法不需要打印语句因为定义时加了运行语句
A = test_mokuai.Temple()
# 实例化后，调用模块-类下面的方法不用加模块名，因为前面实例化的时候已经声明了模块
print(A.sentence)
A.reading()

# 导入模块重命名
# import…as… 比如import test_mokuai太长，就可以用import test_mokuai as tm语句，意思是为“test_mokuai”取个别名为“tm”
import test_mokuai as tm
print(tm.sentence)
tm.mountain()
A = tm.Temple()
print(A.sentence)
A.reading()

# 导入模块中的指定部分，且可以直接使用，无需加上“模块.”前缀
# from（模块名）import（指定模块中的变量名/函数名/类名）
# from（模块名）import * (*代表“模块中所有的变量、函数、类”)
from test_mokuai import Temple
A = Temple() # TypeError: Temple.reading() missing 1 required positional argument: 'self'——不实例化就会出现“类型错误”
A.sentence
A.reading()

# 借用别人的模块
# 打开终端，Windows用户输入pip install + 模块名，点击enter即可
# 打开终端，苹果电脑输入：pip3 install + 模块名，点击enter即可

# 自学模块，将案例做成笔记，如下：
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