# 练习：抓取网站评论
import requests
from bs4 import BeautifulSoup

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/',verify=False) # 对于SSL证书错误的网站，可以忽略验证SSL证书

print(res.status_code)

html = res.text

soup = BeautifulSoup(html,'html.parser')

items = soup.find_all(class_='comment-content')

for item in items:
    pinglun = item.find('p')
    print(pinglun.text)

# 练习：抓取网站分类
import requests
from bs4 import BeautifulSoup
res = requests.get('http://books.toscrape.com/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='nav nav-list')
for item in items:
    fenlei = item.find('ul')
    print(fenlei.text,'\n')

# 练习：抓取书名和评分
import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.huchiu.com/wxapp/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='tabs')
for item in items:
    leibie = item.find(class_='item')
    with open(r'SquidGame\jieguo.txt','w+',encoding='utf-8') as f:
        f.write(leibie.text)