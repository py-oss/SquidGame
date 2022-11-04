# 编码与解码
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

# 文件读取分三步：开——读——关
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

# 文件写入分三步：开——写——关
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

# 文件读写的几种方式
# a+ 追加且可读，ab+ 二进制追加且可读
# w+ 读写，wb+ 二进制读写；以二进制的方式打开一个文件用于写入。因为图片和音频是以二进制的形式保存的，所以使用wb+模式就好了
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

# 小练习：打印每个学生的总成绩
with open('D:\OneDrive\GitHub\SquidGame\scores.txt','r',encoding='utf-8') as file:
    file_lines = file.readlines() # 方法调用记得加（），出现 TypeError: 'builtin_function_or_method' object is not iterable 错误，一般是括号忘记带了
for i in file_lines:
    data = i.split() # 按行读取，记得切分为列表
    sum = 0 #先把总成绩设为0
    for score in data[1:]: #遍历列表中第1个数据和之后的数据
        sum = int(score) + sum #然后依次加起来，但分数是字符串，所以要转换
    res = data[0] + str(sum) #结果就是学生姓名和总分
    print(res)
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

# 成绩从高到低排序
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

# 复制图片
with open('1.jpg','rb') as file1: # 奇怪的是用rb+模式写出来的图片打不开
    filecontent = file1.read()
with open('2.jpg','wb') as file2: # 奇怪的是用wb+模式写出来的图片打不开
    file2.write(filecontent)

# 古诗词填空
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