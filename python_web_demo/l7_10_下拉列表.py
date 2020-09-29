# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 22:05
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_10_下拉列表.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#打开浏览器Chrome
driver = webdriver.Firefox()
#打开网址
driver.get("http://www.baidu.com")
#点击设置，出现拉下列表，悬浮出现的列表，使用定位的快捷键，按住shift+ctrl+c，鼠标点击需要定位的元素
driver.find_element_by_xpath("设置的定位").click()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"下拉列表的元素-高级设置")))
driver.find_element_by_xpath("下拉列表的元素-高级设置").click()
#文档格式，是一个select
#Select类，需要引入from selenium.webdriver.support.ui import Select.三种方式
#等待Select出现
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"select的定位")))
#找到select元素
select_ele = driver.find_element_by_xpath("select的定位")
#初始化select类
s = Select(select_ele)
#1、下标
s.deselect_by_index()
#2、value属性
s.deselect_by_value()
#3、文本内容
s.deselect_by_visible_text()

