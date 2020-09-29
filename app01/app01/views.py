from django.shortcuts import render,HttpResponse
from app01 import models
# def add_book(request):
#     books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
#     print(books, type(books)) # Book object (18)
#     return HttpResponse("<p>数据添加成功！</p>")


#
# def add_book(request):
#     books = models.Book.objects.all()
#     print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
#     return HttpResponse("<p>查找成功！</p>")


# def add_book(request):
#     #  获取出版社对象
#     pub_obj = models.Publish.objects.filter(pk=1).first()
#     #  给书籍的出版社属性publish传出版社对象
#     book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
#     print(book, type(book))
#     return HttpResponse(book, type(book))


def add_book(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)