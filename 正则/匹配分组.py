# -*- coding: utf-8 -*-
# @Time     : 2019/11/2518:26
# @Author   : l7
# @File     : 匹配分组.py
# @Software : PyCharm
import re

'''
|           匹配任意一个表达式
(ab)        将括号中字符作为一个分组
\num        引用分组num匹配到的字符串
(?p<name>)  分组起别名
(?P<name>)  引用别名为name分组匹配到的字符串
'''
