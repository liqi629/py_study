# -*- coding: utf-8 -*-
# @Time     : 2019/12/320:10
# @Author   : l7
# @File     : l7_2_11.py
# @Software : PyCharm

print("------功能菜单------")
print("------1------")
print("计算5个数之和")
print("------2------")
print("计算5个数之平均值")
print("------X------")
print("退出")
while True:
    menu = input("请选择菜单")
    print("已经选择菜单", menu,)

    if menu == "1":
        a = input("请输入第一个数字")
        b = input("请输入第二个数字")
        print("求和是", int(a)+int(b))
    elif menu == "2":
        a = input("请输入第一个数字")
        b = input("请输入第二个数字")
        print("求平均", (int(a)+int(b))/2)
    else:
        print("退出")
        break
