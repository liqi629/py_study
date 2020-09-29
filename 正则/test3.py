# -*- coding: utf-8 -*-
# @Time     : 2019/11/2517:51
# @Author   : l7
# @File     : test3.py
# @Software : PyCharm
import re

# "a" =="""a"  ,返回不是none  是空字符串
res = re.match("\d*", "a")
print(res)

res1 = re.match("\\\\n\w*", "\\nabc")
print(res1)

res2 = re.match(r"\\nabc", "\\nabc")
print(res2)

