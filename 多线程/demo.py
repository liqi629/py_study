# -*- coding: utf-8 -*-
# @Time     : 2019/9/23 20:23
# @Author   : l7
# @File     : demo.py
# @Software : PyCharm
from threading import Thread
import time
import datetime
#
# def est():
#     print("------hahah----------")
#     print()
#     time.sleep(1)
#
# for i in range(5):
#     t = Thread(target=est)
#     t.start()
str = (datetime.datetime.now()+datetime.timedelta(minutes=-1)).strftime('%Y-%m-%d %H:%M')


print(str)
print(type(str))

print(type('2019-10-31 16:58'))
admin = {"user": "admin", "pwd": "admin"}
print(type(admin["pwd"]))