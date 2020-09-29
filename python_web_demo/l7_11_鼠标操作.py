# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 22:20
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_11_鼠标操作.py
# @Software : PyCharm
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#打开浏览器Chrome
driver = webdriver.Firefox()
#打开网址
driver.get("http://www.baidu.com")
#鼠标悬浮设置，出现拉下列表，悬浮出现的列表，使用定位的快捷键，按住shift+ctrl+c，鼠标点击需要定位的元素
#实例化
ac = AC(driver)
#鼠标行为，最后调用perform()来执行鼠标操作
ele = driver.find_element_by_xpath("设置按钮的定位")
ac.move_to_element(ele).perform()
#等待下拉菜单出现，点击
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"下拉列表的元素-高级设置")))
driver.find_element_by_xpath("下拉列表的元素-高级设置").click()


#鼠标拖拽
AC.drag_and_drop()
