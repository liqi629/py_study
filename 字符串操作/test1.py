# -*- coding: utf-8 -*-
# @Time     : 2019/12/221:02
# @Author   : l7
# @File     : test1.py
# @Software : PyCharm

a = "helloA"

#取左不取右   m，n，k  k默认1
# 倒叙输出
print(a[2:4:])
print(a[4::-1])
print(a[::-1])
# 大小写
print(a.upper())
print(a.lower())

#查找字符串,找到返回索引，否则-1，子字符串 返回首字母的索引
b = "hello is alsjodasdoasf"
print(b.find("a"))
print(b.find("aw"))
print(b.find("is"))

#字符串替换,替换次数，不指定，全部替换
c = b.replace("o", "O",2)
print(c)