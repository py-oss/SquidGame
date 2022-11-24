# 爬虫核心工作原理
# 1. 获取数据：发起请求，返回数据（1）
# 2. 解析数据：解析成我们能读懂的格式（2/3/4/5）
# 3. 提取数据：提取我们需要的数据（2/3/4/5）
# 4. 存储数据：保存便于使用（6）

# response对象的常用属性之一：res.status_code，检查请求是否成功
import requests
res = requests.get('https://www.163.com/dy/article/GQMMTS1P0552LY0M.html') 
# 打印变量res的响应状态码，以检查请求是否成功
print(res.status_code) # response.status_code 检查网址状态

# response对象的常用属性之二：res.content，适用于图片、音频、视频的下载
import requests
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png') # 发出请求，把结果存在变量中
pic = res.content # 把response对象内容以二进制形式返回
with open(r'SquidGame\1.jpg','wb') as f: # 加encdoing=''报错：ValueError: binary mode doesn't take an encoding argument--ValueError:二进制模式不采用编码参数；需要加路径，并且路径前加r才不会报错：OSError: [Errno 22] Invalid argument: 'SquidGame\x01.jpg'--OSError:[Erno 22]无效参数：“SquidGame\x01.jpg”
    f.write(pic) # 操作导出文件

# response对象的常用属性之三：res.text，适用于文字、网页源代码的下载
import requests
res = requests.get('https://www.v2gr.com/p/71353.html')
txt1 = res.text
with open(r'SquidGame\1.txt','w+',encoding='utf-8') as f:
    f.write(txt1)

# response对象常用属性之四：res.encoding，定义Response对象的编码
import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res.encoding='utf-8' # 定义Reponse对象的编码为utf-8，遇上文本的乱码问题，才考虑用res.encoding
novel=res.text # 把Response对象的内容以字符串的形式返回
print(novel[:800]) # 打印小说的前800个字

# 我的设计
import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html1 = res.text
with open(r'SquidGame\1.html','w+',encoding='utf-8') as f:
    f.write(html1)

# 老师的设计
# 调用requests模块
import requests
# 获取网页源代码，得到的res是response对象。
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 检测请求是否正确响应
print(res.status_code)
# 正确响应，进行读写操作
# 新建一个名为book的html文档，你看到这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 字符串需要以w读写。你在学习open()函数时接触过它。
if res.status_code == 200:
    file = open('book.html','w')
    # res.text是字符串格式，把它写入文件内。
    file.write(res.text)
    # 关闭文件
    file.close()