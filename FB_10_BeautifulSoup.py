# 操作诀窍1：逐步打印，检查错误，百度方法
# 操作诀窍2：res————bs————list————tag

# 提取数据的两种思路：
# 1 - 将想要的数据分别提取再做组合
# 2 - 寻找共同最小父级标签提取数据
# 在爬虫实践当中，其实常常会因为标签选取不当，或者网页本身的编写没做好板块区分，你可能会多提取到出一些奇怪的东西。
# 一般有两种处理方案：数量太多而无规律，我们会换个标签提取；数量不多而有规律，我们会对提取的结果进行筛选——只要列表中的若干个元素就好。

# BeautifulSoup如何解析数据
# 操作对象：URL链接——Response对象————字符串——BS对象——由Tag组成的列表——Tag对象
# bs对象 = BeautifulSoup(解析的数据,'解析器')
import requests
from bs4 import BeautifulSoup
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/',verify=False) # 对于SSL证书错误的网站，可以忽略验证SSL证书
# print(res.status_code) # 测试网址是否能连通
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='comment-content')
for item in items:
    pinglun = item.find('p')
    print(pinglun.text)

# BeautifulSoup如何提取数据
# find()，提取满足要求的首个数据；用法：bs对象(标签,属性)
    # 例子：soup.find('div',class='books')
    # class_写法是为了和Python自带的Class类的写法作区分
    # 除了可以用class_属性，还可以用style_属性去匹配
    # 标签和属性可以任选其一，取决于要在网页中提取的内容：一个参数可以定位内容就用一个参数；两个参数一起才能定位内容就两个参数一起用
# find_all()，提取满足要求的所有数据；用法：bs对象(标签,属性)
    # 例子：soup.find_all('div',class='books')
import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/')
res.encoding = res.apparent_encoding # 强制转码
# print(res) # 打印测试获取网址内容
html = res.text
# print(html) # 打印测试获取网址文本
soup = BeautifulSoup(html,'html.parser')
# print(soup) # 打印测试解析对象
items = soup.find_all(class_='nav nav-list')
# print(items) # 打印测试解析属性内容
# for item in items:
#     fenlei = item.find('ul')
#     print(fenlei.text + '\n') # 打印测试获取的结果
with open(r'jieguo.txt','w+',encoding='utf-8') as f:
    for item in items:
        fenlei = item.find('ul')
        f.write(fenlei.text + '\n')

# BeautifulSoup的Tag对象
    # Tag.find()和Tag.find_all()，提取Tag中的Tag
    # Tag.text，提取Tag中的文字
    # Tag['属性名']，提取Tag中这个属性的值
import requests 
from bs4 import BeautifulSoup 
res =requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html=res.text
soup = BeautifulSoup( html,'html.parser')
items = soup.find_all(class_='books')  
for item in items:                     
    kind = item.find('h2')             
    title = item.find(class_='title')  
    brief = item.find(class_='info')      
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text) 

# 练习1-获取评论
import requests
from bs4 import BeautifulSoup
url_destnation = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/'
res_comment = requests.get (url_destnation)
bs_comment = BeautifulSoup(res_comment.text,'html.parser')
list_comments = bs_comment.find_all('div',class_= 'comment-content')
for tag_comment in list_comments:
    print(tag_comment.text)

# 练习2-获取分类
# 我的设计
import requests
from bs4 import BeautifulSoup
res_fenlei = requests.get('http://books.toscrape.com/')
# print(res_fenlei)
bs_fenlei = BeautifulSoup(res_fenlei.text,'html.parser') # 注意使用bs对象.text方法，获取页面字符串
# print(bs_fenlei)
list_fenlei = bs_fenlei.find('ul',class_='nav nav-list').find('ul').find_all('li')
for fenlei in list_fenlei:
    print(fenlei.text.strip())

# 老师的设计
import requests
from bs4 import BeautifulSoup
res_bookstore = requests.get('http://books.toscrape.com/')
bs_bookstore = BeautifulSoup(res_bookstore.text,'html.parser')
list_kind = bs_bookstore.find('ul',class_='nav').find('ul').find_all('li') # 这里需要提取好几层
for tag_kind in list_kind:
    tag_name = tag_kind.find('a')
    print(tag_name.text.strip()) # 去除特殊字符串，比如空格，\n，\t等等

# 练习3-获取书名、价格和评分
# 我的设计
import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
res.encoding = res.apparent_encoding
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3').find('article',class_='product_pod')
# print(items)
for item in items:
    shuming = item.find('h3').find('a')
    jiage = item.find('div',class_='product_price').find('p',class_='price_color')
    pingfen = item.find('p',class_='star-rating')['class'][1] #例如：<p class="star-rating Two">,<p>标签中的'class'属性中有'star-rating'和'two'两个属性值 # 这一步不会做，其实可以靠逐步打印结果来寻找方法
    #此时只提取一个属性值，其中'star-rating'是第0个属性值，'two'是1个
    print(shuming['title'],'\n',jiage.text,'\n',pingfen)

# 老师的设计
import requests
from bs4 import BeautifulSoup
res_bookstore = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
bs_bookstore = BeautifulSoup(res_bookstore.text,'html.parser')
list_books = bs_bookstore.find_all(class_='product_pod')
for tag_books in list_books:
    tag_name = tag_books.find('h3').find('a') # 找到a标签需要提取两次
    list_star = tag_books.find('p',class_="star-rating")
    # 这个p标签的class属性有两种："star-rating"，以及具体的几星比如"Two"。我们选择所有书都有的class属性："star-rating"
    tag_price = tag_books.find('p',class_="price_color") # 价格比较好找，根据属性提取，或者标签与属性一起都可以
    print(tag_name['title']) # 这里用到了tag['属性名']提取属性值
    print('star-rating:',list_star['class'][1])
    # 同样是用属性名提取属性值
    # 用list_star['class']提取出来之后是一个由两个值组成的列表，如："['star-rating', 'Two']"，我们最终要提取的是这个列表的第1个值："Two"。
    # 为什么是列表呢？因为这里的class属性有两个值。其实，在这个过程中，我们是使用class属性的第一个值提取出了第二个值。
    print('Price:',tag_price.text, end='\n'+'------'+'\n') # 打印的时候，我加上了换行，为了让数据更加清晰地分隔开，当然你也可以不加。

# 练习4-获取文章发布时间、标题和链接
# 我的设计
import requests
from bs4 import BeautifulSoup
res_wenzhang = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
bs_wenzhang = BeautifulSoup(res_wenzhang.text,'html.parser') # 将字符串解析成bs对象，所以不要忘记.text方法
# blog_wenzhang = bs_wenzhang.text # 到这里解析出来的都是文字，没有html符号可以定位
# print(blog_wenzhang)
blog_wenzhang = bs_wenzhang.find_all('article',class_='post')
# print(blog_wenzhang)
for wenzhang in blog_wenzhang:
    biaoti = wenzhang.find('h2',class_='entry-title')
    shijian = wenzhang.find('time',class_='entry-date published')
    lianjie = wenzhang.find('h2',class_='entry-title').find('a')
    print(biaoti.text,'\n',shijian.text,'\n',lianjie['href'])

# 老师的设计
import requests
from bs4 import BeautifulSoup
url_destnation = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/'
res_destnation = requests.get(url_destnation)
print(res_destnation.status_code) # 打印响应码
bs_articles = BeautifulSoup(res_destnation.text,'html.parser')
list_articles = bs_articles.find_all('header', class_ = "entry-header") # 首先找到每篇文章所在的相同的元素
for tag_article in list_articles: # 遍历列表
    tag_title = tag_article.find('h2',class_ = "entry-title") # 找文章标题
    tag_url = tag_article.find('a',rel = "bookmark")  # 找文章链接
    tag_date = tag_article.find('time',class_="entry-date published") # 找文章发布时间
    print(tag_title.text,'发布于：',tag_date.text) # 打印文章标题与发布时间
    print(tag_url['href'])  # 换行打印文章链接，需要使用属性名提取属性值

# 解密下厨房
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
res_caipu = requests.get('https://www.xiachufang.com/explore/',headers=headers)
bs_caipu = BeautifulSoup(res_caipu.text,'html.parser')
list_caipu = bs_caipu.find_all('div',class_='info pure-u')
list_all = []
for tag_caipu in list_caipu:
    tag_caiming = tag_caipu.find('p',class_='name')
    tag_url = tag_caipu.find('a')
    tag_shicai = tag_caipu.find('p',class_='ing ellipsis')
    caiming = tag_caiming.text.strip()
    url = 'https://www.xiachufang.com'+tag_url['href']
    shicai = tag_shicai.text
    list_all.append([caiming,url,shicai])
print(list_all)

# 另一种思路：分别提取所有的菜名、所有的URL、所有的食材。然后让菜名、URL、食材给一一对应起来
# 创建一个空列表，启动循环，循环长度等于<p>标签的总数——你可以借助range(len())语法。
# 在每一次的循环里，去提取一份菜名、URL、食材。拼接为小列表，小列表拼接成大列表。输出打印。
# 通过遍历偏移量来对应数据
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res_foods = requests.get('http://www.xiachufang.com/explore/',headers=headers)
bs_foods = BeautifulSoup(res_foods.text,'html.parser') # 解析器只能解析字符串
tag_name = bs_foods.find_all('p',class_='name')
tag_ingredients = bs_foods.find_all('p',class_='ing ellipsis')
list_all = []
for x in range(len(tag_name)):
    list_food = [tag_name[x].text.strip(),tag_name[x].find('a')['href'],tag_ingredients[x].text.strip()] 
    list_all.append(list_food)
print(list_all)

# 抓取网页小练习发现的知识点
# 正确做法：寻找最小共同父级标签
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res_xcx = requests.get('http://www.weimob.com/marketing/xcxdj',headers=headers)
bs_xcx = BeautifulSoup(res_xcx.text,'html.parser')
list_xcx = bs_xcx.find_all(class_='mr-[10px] flex h-[40px] w-[125px] items-center justify-center rounded-[8px] rounded-tl-[0px] bg-[#fff] text-[14px] text-[#606060] transition-colors hover:bg-[#287AF8] hover:text-[#fff]')
# print(list_xcx) # 列表没有.text的对应属性
with open(r'/Users/wjy/Library/CloudStorage/OneDrive-个人/SquidGame/jieguo.txt','w+',encoding='utf-8') as f:
    for tag_xcx in list_xcx: # 遍历之后为单个元素，单个元素可以获取.text属性值
        # tag_item = tag_xcx
        # print(tag_zj)
        f.write(tag_xcx.text + '\n')

# 错误做法：tag_xcx数据类型不能find之后find_all==》tag数据不能定位之后再定位，因为已经被遍历成单个元素了
# list_xcx数据类型可以find之后find_all==》因为list是一个列表，可以定位之后再定位
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res_xcx = requests.get('http://www.weimob.com/marketing/xcxdj',headers=headers)
bs_xcx = BeautifulSoup(res_xcx.text,'html.parser')
list_xcx = bs_xcx.find_all(class_='mb-[40px] last:mb-[0px]')
# print(list_xcx)
with open(r'jieguo.txt','w+',encoding='utf-8') as f:
    for tag_xcx in list_xcx:
        tag_zj = tag_xcx.find(class_='mt-[17px] flex w-[680px] flex-wrap').find_all('mr-[10px] flex h-[40px] w-[125px] items-center justify-center rounded-[8px] rounded-tl-[0px] bg-[#fff] text-[14px] text-[#606060] transition-colors hover:bg-[#287AF8] hover:text-[#fff]')
        f.write(tag_zj.text + '\n')

# 练习1-豆瓣电影爬虫
# 解法1-寻找最小共同父级标签
import requests, bs4
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span',class_="rating_num").text
        url_movie = titles.find('a')['href']
        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
# 解法2：分别提取数据再做组合
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    tag_num = bs.find_all('div', class_="item")
    tag_comment = bs.find_all('div', class_='star')
    tag_word = bs.find_all('span', class_='inq')
    list_all = []
    for x in range(len(tag_num)):
        if tag_num[x].text[2:5] == '' or tag_num[x].text[2:5] =='' or x >= len(tag_word):
            list_movie = [tag_num[x].text[2:5], tag_num[x].find('img')['alt'], tag_comment[x].text[2:5], tag_num[x].find('a')['href'] ]
        else:
            list_movie = [tag_num[x].text[2:5], tag_num[x].find('img')['alt'], tag_comment[x].text[2:5], tag_word[x].text, tag_num[x].find('a')['href']]
        list_all.append(list_movie)
    print(list_all)