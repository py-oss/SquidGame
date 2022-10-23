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
class AuthorManager:

    authors = []
    # 创建一个存放作者名的列表
    def __init__(self):
        book1 = Book('撒哈拉的故事','三毛','我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book2 = Book('梦里花落知多少','三毛','人人都曾拥有荷西，虽然他终会离去。')
        book3 = Book('月亮与六便士','毛姆','满地都是六便士，他却抬头看见了月亮。')
        self.books = [book1,book2,book3]
        # 将三个实例放在列表books里
        self.authors.append(book1.author)
        self.authors.append(book2.author)
        self.authors.append(book3.author)
        # 将三个实例的作者名添加到列表author里
 
    def authormenu(self):
        while True:
            print('1.查询书籍')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_author_book()
                # 调用方法
            else:
                print('感谢使用！')
                break
 
    def show_author_book(self):
        author = input('你想找谁的书呢？')
        if author in self.authors:
            for book in self.books:
                if book.author == author:
                    print(book)
        else:
            print('很可惜，我们暂时没有收录这位作者的作品')

BookManager1 = AuthorManager() # 对象实例化
BookManager1.authormenu()