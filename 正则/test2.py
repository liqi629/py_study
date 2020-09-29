# -*- coding: utf-8 -*-
# @Time     : 2019/11/2516:46
# @Author   : l7
# @File     : test2.py
# @Software : PyCharm
import re

res = re.match(".", "i")
print(res)

# 不能是\n
res1 = re.match(".", "\n")
print(res1)

'''
. 匹配任意1个字符  除了\n
[] 匹配【】中列举的字符
\d 匹配数字 0-9
\D 匹配非数字
\s 匹配空白  即空格 tab键  \n \t \r
\S 匹配非空白
\w 匹配单词字符 a-z  A-Z 0-9 _
\W 匹配非单词字符
'''
res2 = re.match("..", "ab")
print(res2)

res3 = re.match("\d", "1")
print(res3)

res4 = re.match("\S\d", "g1")
print(res4)
# 手机号
res5 = re.match("1\d\d\d\d\d\d\d\d\d\d", "18619999999")
print(res5)
res6 = re.match("1[34578]\d\d\d\d\d\d\d\d\d", "18619999999")
print(res6)

res7 = re.match("1[^358]\d\d\d\d\d\d\d\d\d", "11619999999")
print(res7)


res8 = re.match("1[a-z5-9]\d\d\d\d\d\d\d\d\d", "15619999999")
print(res8)

'''
\d == [0-9]
\D == [^0-9]
\w == [a-zA-Z0-9_]
'''

'''
数量信息
* 0次或无限次 即可有可无
+ 至少1次
? 要么1次要么0次
{m} m次
{m，} 至少m次
{m，n} 从m到n次

'''
res9 = re.match("1[a-z5-9]\d*", "15611234567")
print(res9)
res10 = re.match("1[a-z5-9]\d*", "15")
print(res10)

res11 = re.match("1[a-z5-9]\d+", "151")
print(res11)

res12 = re.match("1[a-z5-9]\d？", "15111")
print(res12)

res13 = re.match("1[a-z5-9]\d{2}[a]", "15112a")
print(res13)

res14 = re.match("1[a-z5-9]\d{2,}", "151")
print(res14)
res15 = re.match("1[a-z5-9]\d{2,3}", "151234")
print(res15)