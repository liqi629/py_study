# -*- coding: utf-8 -*-
# @Time     : 2019/8/20 11:38
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : 迭代器.py
# @Software : PyCharm
# def findMinAndMax(L):
#     if L==[]:
#
#             return (None,None)
#     else:
#
#         min = L[0]
#
#         max = L[0]
#
#         for nums in L:
#
#             if nums <= min:
#
#                 min = nums
#
#         for nums in L:
#
#             if nums >= max:
#
#                 max = nums
#
#         return (min, max)
# L=(1,2,4,6,8,11,3,45,78)
# a=findMinAndMax(L)
# print(a)


import os
import time
ret = os.fork()

if ret == 0:
    while True:
        print("---1---")
        time.sleep(1)

else:

    while True:
        print("---2---")
        time.sleep(1)