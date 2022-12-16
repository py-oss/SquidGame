# Network，记录浏览器的所有请求，ALL（查看全部）/XHR（仅查看XHR）/Doc（Document，第0个请求一般在这里）

# XHR/Fetch，传输数据，不必刷新/跳转网页，即可加载新的内容
    # Headers--General：获取第0个请求的链接

# json，数据格式，形式：字典和列表的结合体
    # 如何找包含需要的json数据：
    # 1 - 看名字判断
    # 2 - 看文件大小，文件大一般包含需要的数据
    # 3 - preview看，或者一层层点开看
    # 4 - 先把Network面板清空，操作加载新的XHR

# 操作诀窍：res————json————list————tag

# 老师的设计1
import requests
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
json_music = res_music.json()
list_music = json_music['data']['song']['list']
for music in list_music:
    print(music['name'])

# 老师的设计2
import requests
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 使用json()方法，将response对象，转为列表/字典
json_music = res_music.json()
# 一层一层地取字典，获取歌单列表
list_music = json_music['data']['song']['list']
# list_music是一个列表，music是它里面的元素
for music in list_music:
    # 以name为键，查找歌曲名
    print(music['name'])
    # 查找专辑名
    print('所属专辑：'+music['album']['name'])
    # 查找播放时长
    print('播放时长：'+str(music['interval'])+'秒')
    # 查找播放链接
    print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')

# 我的设计
import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
res_gedan = requests.get('https://u.y.qq.com/cgi-bin/musics.fcg?_=1670934723284&sign=zzb1973d95antrpxrtytyhmwg373ruqw817f2183',headers=headers)
json_gedan = res_gedan.json()
# print(json_gedan)
list_gedan = json_gedan['req_1']['data']['body']['song']['list']
# print(list_gedan)
for gequ in list_gedan:
    print(gequ['name'])

# json
# 引入json模块
import json
# 创建一个列表a
a = [1,2,3,4]
# 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b
b = json.dumps(a)
# 打印b
print(b)
# 打印b的数据类型
print(type(b))
# 使用loads()函数，将json格式的字符串b转为列表，赋值给c
c = json.loads(b)
# 打印c
print(c)
# 打印c的数据类型
print(type(c)) 

# 翻页提取更多数据

import requests
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头
params = {
'ct':'24',
'qqmusic_ver': '1298',
'new_json':'1',
'remoteplace':'sizer.yqq.song_next',
'searchid':'59091538798969282',
't':'0',
'aggr':'1',
'cr':'1',
'catZhida':'1',
'lossless':'0',
'flag_qc':'0',
'p':'1',
'n':'20',
'w':'周杰伦',
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'utf-8',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0'    
}
# 将参数封装为字典
res_music = requests.get(url,headers=headers,params=params)
# 发起请求，填入请求头和参数
