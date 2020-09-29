# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 21:10
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_01_基础调用，熟悉底层源码.py
# @Software : PyCharm
#python selenium 库 ======驱动程序  ====浏览器
#http通信
from selenium import webdriver
#打开浏览器Chrome
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")
#寻找元素（id方式）-点击
driver.find_element_by_id().click()