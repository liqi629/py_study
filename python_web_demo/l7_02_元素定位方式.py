# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 21:36
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_02_元素定位方式.py
# @Software : PyCharm
from selenium import webdriver
#打开浏览器Chrome
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")
#元素定位
#1、id
driver.find_element_by_id()
#2、class_name 参数只能是一个class值
driver.find_element_by_class_name()
#找页面当中匹配表达式的所有   返回的是列表  按照下标取值
driver.find_elements_by_class_name()
#3、tag
driver.find_element_by_tag_name()
#4、name
driver.find_element_by_name()
#5、6   针对a元素  通过a元素文本内容匹配
driver.find_element_by_link_text()#全匹配
driver.find_element_by_partial_link_text()#模糊
#7、xpath
driver.find_element_by_xpath()
#8、css_selector
driver.find_element_by_css_selector()