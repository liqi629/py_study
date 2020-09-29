# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 23:06
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_06_元素等待_1.py
# @Software : PyCharm
from selenium import webdriver
import time
#打开浏览器Chrome
driver = webdriver.Chrome()
#隐性等待，打开浏览器会话 就要设置，全局可用。等待一个元素被找到、被调用。不能等alert弹窗
driver.implicitly_wait(10)
#打开网址
driver.get("http://www.baidu.com")
#点击登录
driver.find_element_by_name("tj_login").click()
#等待登录弹出窗
#强制等待，写在哪，哪里就生效
time.sleep(2)
#选择用户名登录，点击
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
#点击用户名输入框
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("夜舞天缘")
#点击密码输入框，输入密码
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("xxxxx")


#关闭浏览器
driver.quit()