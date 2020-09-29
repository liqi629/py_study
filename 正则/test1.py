# -*- coding: utf-8 -*-
# @Time     : 2019/11/2516:23
# @Author   : l7
# @File     : test1.py
# @Software : PyCharm
import re


pattern = "itcast"
string = "itcastasdfsdf"
# match方法进行匹配操作,从左往右匹配，匹配完成，字符串有多余的也不影响
result = re.match(pattern, string)
# print(result)
print(dir(result))
# 如果上一步匹配到数据，可以使用group方法来提取数据
print(result.group())



