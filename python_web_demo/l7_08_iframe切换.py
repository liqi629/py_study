# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 0:10
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_08_iframe切换.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#元素定位后，查看历史标签有没有iframe标签，有，就要进行切换。
#定位的时候，虽然可以定位，但是代码执行的时候，必须切换后，才能点击
#1、判断元素是否在iframe里面


#打开浏览器Chrome
driver = webdriver.Firefox()
#方式一：
#2、切换
driver.switch_to.frame(2)   #下标
driver.switch_to.frame("")  #iframe属性值
# 页面元素对象  find_element_by_xpath("xpath表达式")，返回的是一个页面对象
driver.switch_to.frame(driver.find_element_by_xpath("xpath表达式"))

#退出iframe，回到原来的html页面
driver.switch_to_default_content()

#如果进入iframe后，在iframe页面又进入了iframe
#切换回第一层iframe。如果没有上一级 ，就保留当前页面
driver.switch_to.parent_frame()

#方式二：切换
#加入显性等待，确认一下iframe是否出现。
# 条件：EC.frame_to_be_available_and_switch_to_it，传入的参数，上述3种(下标、元素定位、xpath)都可以，函数自己判断了
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it())
driver.find_element_by_xpath("XXX")






