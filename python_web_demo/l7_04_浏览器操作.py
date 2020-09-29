# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 22:42
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_04_浏览器操作.py
# @Software : PyCharm
from selenium import webdriver
#打开浏览器Chrome
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")
#全屏
driver.maximize_window()
driver.get("http://www.taobao.com")
#前进
driver.forward()
#后退
driver.back()
#刷新
driver.refresh()
#获取窗口标题
print(driver.title)
#获取当前窗口url
print(driver.current_url)
#获取当前窗口的句柄
print(driver.current_window_handle)
#关闭浏览器当前窗口
driver.close()


#关闭整个浏览器会话
driver.quit()
