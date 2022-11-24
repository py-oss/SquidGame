# print()函数 功能：打印内容
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

# input()函数 功能：输入数据
'''
有问有答，有来有往；
函数好用，赋值第一；
返回类型，必为str
想要整数，源头转换
'''
magic = input('请在以下选项【厄里斯魔镜；时间转换器；飞天扫帚；隐形斗篷】中，选择出你最想拥有的魔法物品：')
print(magic+'是我最想拥有的魔法！')

# 变量
# 变量必须先声明并赋值才能使用
# 为什么？不声明计算机怎么知道你的数据类型是什么呢？
a = 5 # 赋值用【=】号表示
b = 10
a = b # 变量命名要规范
print(a) # 变量的最终值等于最后赋值的值

# 数据类型
'''
只要被引号（单引号/双引号/三引号）括起来的数据都是字符串，用str表示
没有小数点的数字统称为整数，运算结果永远精确，用int表示
有小数点的数字统称为浮点数，运算有四舍五入的误差，用float表示
'''

'''
数据拼接：+
只能拼接字符串类型的数据，其他数据类型不能拼接
“圈子不同，不能相融”
'''

''' type()函数
作用：查询数据类型，Python是一门面向对象编程的语言，只有知道是什么对象，才能调用相关的对象属性和方法
语法：print(type('放入需要查询的数据'))
'''

# 布尔值 True 和 False
'''
1. 计算机判断真假的过程叫做布尔运算
2. 布尔运算会产生【True】和【False】的布尔值
3. True和False就像开关，决定if语句和while语句是否运行
'''
# bool()函数 用来判断数据的真假，和type()的用法类似
print(bool(''))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(None))

# 列表 适用所有增删查改语句：左右空，取到头；左要取，右不取
## 靠“偏移量”取值，可迭代对象，可用for……in……循环来遍历
'''
列表名 命名需能一眼判断是什么数据
赋值号 将列表内的数据赋值给变量
中括号 用中括号区分列表的整体数据结构
逗号 用逗号间隔列表内元素
'''
students = ['晓敏',18.8,42] # 列表很包容，字符串/整数/浮点数都可以放进去
print(type(students))
print(type(students[0]))
print(type(students[1]))
print(type(students[2]))
### 切片（查） 将列表的某个片段拿出来处理，切片后的列表也是列表
students = ['晓敏',18.8,42]
print(students[:])
print(students[0:1])
print(students[1:])
print(students[:1])
print(students[1:2])
print(students[:0]) # 超出列表范围取出来为空列表
print(type(students[3:])) # 空列表也是列表
### 增
students = ['晓敏',18.8,42]
students.append(['小米','小美'])
print(students)
# 给列表增加元素语法为：列表名.append(元素)
# append()函数只能追加一个元素进去
# 该元素可以是字符串/整数/浮点数/列表
# 因此，列表理论上长度可变，容量无限
### 删
del students[0] # del 列表名[元素索引]
print(students) # del 列表名 可以删除整个列表
del students['小米'] # del 无法直接删除指定的某元素，必须通过元素的索引才能操作
print(students) # 报错：类型错误。 只能是整数或者切片，不能使用字符串

# 字典
## 靠“键”取值，可迭代对象，可用for……in……循环来遍历
'''
字典名 需要一眼知道命名用来做什么
赋值号 将数据赋值给变量
花括号 用来区分字典的整体数据结构
逗号 用来区分字典内的数据结构
冒号 字典内的单个元素数据是由键值对组成，用冒号区分开键值
'''
scores = {'小明':96,'小红':90,'小刚':90}
print(len(scores)) # len()函数可以取得字典或列表的长度
# 字典的键是唯一的，值可以重复；如果命名了相同的键，后面的值会覆盖前面的值
### 查
scores = {'小静':28,'小张':99,'小怡':87}
print(scores['小张'])
print(scores[0]) # traceback回溯错误，发现keyerror键错误，证明字典取值只能靠键
### 删
scores = {'小刚':60,'小明':88,'小红':22}
del scores['小刚'] # del 字典名[键] 即可删除指定的键值对
print(scores)
### 增
scores ['小艺'] = 66 # 字典名[键] = 值
print(scores) # 可直接在字典末尾追加一行数据
### 改
scores ['小明'] = 92 # 字典名[键] = 值
scores ['小红'] = 72 # 可修改指定键的值
print(scores) # 上述区别在于，已存在的会覆盖新的键值对；不存在的会在末尾追加新的键值对

# 列表和字典对比
'''
1. 修改都用同样的赋值语句
2. 都支持任意嵌套，可嵌套数据可以是列表也可以是数据
'''
scores1 = [18,19,20]
scores2 = [19,20,18]
print(scores1 == scores2) # 列表有序，偏移定位
scores3 = {'小明':167,'小刚':188,'小红':158}
scores4 = {'小红':158,'小明':167,'小刚':188}
print(scores3 == scores4) # 字典无序，键来取值

# 元组 可迭代对象，可用for……in……循环来遍历
# 将数据放在小括号()中，它的用法和列表用法类似，主要区别在于：列表中的元素可修改，元组中的元素不可更改。
tuple1 = ('晓敏',18.8,42)
for i in tuple1:
    print(i)

# 数据转换
### str() 将其他数据类型转换成字符串
b = 42
print(type(str(b)))
print(type('42')) # 也可以直接使用引号转换为字符串
# 当我们使用引号时，引号里的东西，都会被强制转换为字符串格式
# 如果引号内放入变量名b，将被强制转换为字符串的是b，而不是数字42

### int() 只有符合整数规范的数据可以被转换成整数，浮点数会强制取整转换
number1 = '1'
number2 = '2'
print(int(number1)+int(number2))
print(type(int(number1)))
print(type(int('2')))
print(int(3.8))
# 浮点数也被int()函数强制转换，但会直接抹零取整数，比如上面的代码输出结果为 3
print(int('1.55'))
# 文本类和小数类字符串无法被转换；以上代码会报错，无法转换

### float() 可将整数和符合数字规范的字符串转换为浮点数
print(type(188))
print(type(float(188)))

# 格式化字符串
# % 格式化：str % ()
print('%s%d'%('数字：',0))
print('%d，%d'%(0,1))
print('%d，%d，%d'%(0,1,0))
# %f的意思是格式化字符串为浮点型，%.1f的意思是格式化字符串为浮点型，并保留1位小数。

name1 = 'Python'
print('I am learning %s'% name1)  # 注：当只跟一个数据时，%后可不加括号，format()一定要有。

# format()格式化函数：str.format()
print('\n{}{}'.format('数字：',0))  # 优势1：不用担心用错类型码。
print('{}，{}'.format(0,1))  # 不设置指定位置时，默认按顺序对应。
print('{1}，{0}'.format(0,1))  # 优势2：当设置指定位置时，按指定的对应。
print('{0}，{1}，{0}'.format(0,1))  # 优势3：可多次调用format后的数据。

name2 =  'Python基础语法'
print('我正在学{}'.format(name2))  # format()函数也接受通过参数传入数据。