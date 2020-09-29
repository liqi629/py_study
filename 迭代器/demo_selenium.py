
# -*- coding: utf-8 -*-
# @Time     : 2019/8/28 9:40
# @Author   : l7
# @File     : demo_selenium.py
# @Software : PyCharm

from selenium import webdriver
#元素定位By
from selenium.webdriver.common.by import By
#等待
from selenium.webdriver.support.wait import WebDriverWait
#等待可见
from selenium.webdriver.support import expected_conditions as EC
#打开浏览器
driver = webdriver.Chrome()
#访问网站
driver.get('http://confluence.yoyosys.com.cn:8090')
#找到用户名输入框，输入用户名
WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.ID,'os_username')))
driver.find_element(By.ID,'os_username').send_keys('li.qi')
#找到密码输入框，输入密码
driver.find_element_by_id('os_password').send_keys('yoyo1234567')
#点击登录按钮
driver.find_element_by_id('loginButton').click()
#关闭浏览器
driver.quit()