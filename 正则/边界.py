# -*- coding: utf-8 -*-
# @Time     : 2019/11/2518:04
# @Author   : l7
# @File     : 边界.py
# @Software : PyCharm
import re

'''
^ 匹配字符串开头
$ 匹配字符串结尾
\b 匹配一个单词的边界
\B 匹配非单词边界
'''

res = re.match(r"1[358]\d{9}$", "18610430456")
print(res)

res1 = re.match(r"^1[358]\d{9}$", "18610430456")
print(res1)

res2 = re.match(r"^\w+\s\bve\B", "ho ver")
print(res2)