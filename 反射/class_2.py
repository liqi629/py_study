# -*- coding: utf-8 -*-
# @Time     : 2019/11/420:27
# @Author   : l7
# @File     : class_2.py
# @Software : PyCharm
from 反射.class_1 import fanshe

setattr(fanshe, "b", 100)

b1 = getattr(fanshe,"b")
setattr(fanshe, "c", 1100)

c1 = getattr(fanshe,"c")
print(c1)