# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 22:52
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_05_元素操作.py
# @Software : PyCharm
from selenium import webdriver
import time
#打开浏览器Chrome
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")

#3、获取属性值
value = driver.find_element_by_id("su").get_attribute("value")
print(value)
#4、获取文本内容
text = driver.find_element_by_id("su").text
#1、输入，输入框属性值"kw"
driver.find_element_by_id("kw").send_keys("hello")
#2、点击，搜索按钮属性值"su"
driver.find_element_by_id("su").click()

time.sleep(2)
driver.quit()
