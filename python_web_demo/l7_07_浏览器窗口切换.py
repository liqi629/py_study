# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 23:35
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_07_浏览器窗口切换.py
# @Software : PyCharm
#代码运行，打开新的窗口，不会自动到新窗口进行操作，需要使用代码进行切换操作
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#打开浏览器Chrome
driver = webdriver.Firefox()
#打开网址
driver.get("http://www.baidu.com")
#1、输入，输入框属性值"kw"
driver.find_element_by_id("kw").send_keys("hello")
#2、点击，搜索按钮属性值"su"
driver.find_element_by_id("su").click()
#显性等待
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="_百度翻译"]')))
#1、获取所有的窗口
windows = driver.window_handles
print("目前所有的窗口：",windows)
#点击
driver.find_element_by_xpath('//a[text()="_百度翻译"]').click()
# time.sleep(2)#不等待，速度太快，无法获取新打开的窗口句柄，也可使用EC.new_window_is_opened
#判断新 窗口是否打开，等待新窗口出现
WebDriverWait(driver,10).until(EC.new_window_is_opened(windows))

#打印当前的窗口
cur_windpws = driver.current_window_handle
print(cur_windpws)
#切换到最新打开的窗口
driver.switch_to.window(windows[-1])
#打印当前的窗口
print(driver.current_window_handle)
time.sleep(2)
driver.quit()