# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 22:30
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_12_键盘操作.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#打开浏览器Chrome
driver = webdriver.Firefox()
#打开网址
driver.get("http://www.baidu.com")

#导入键盘操作的库：from selenium.webdriver.common.keys import Keys
driver.find_element_by_xpath("xxxx").send_keys(Keys.CONTROL,'a') #Ctrl+A  全选
driver.find_element_by_xpath("xxxx").send_keys(Keys.CONTROL,'c') #Ctrl+C  复制
driver.find_element_by_xpath("xxxx").send_keys(Keys.ENTER) #回车
driver.find_element_by_xpath("xxxx").send_keys(Keys.F5) #刷新



driver.find_element_by_xpath("xxxx").send_keys(Keys.CONTROL) #ctrl 待验证？
