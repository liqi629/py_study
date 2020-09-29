# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 23:20
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_06_元素等待_2.py
# @Software : PyCharm
from selenium import webdriver
#导入显性等待相关的三个库
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#打开浏览器Chrome
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")
#点击登录
driver.find_element_by_name("tj_login").click()
#显性等待
#等待登录弹出窗
#等待元素可见visibility_of_element_located，传入定位方式和表达式，使用一个元祖
locator = (By.ID,"TANGRAM__PSP_10__footerULoginBtn")
#条件：EC.visibility_of_element_located(locator)，放入until
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
#等待元素存在
# EC.presence_of_element_located
#等待元素可点击
# EC.element_to_be_clickable

#选择用户名登录，点击
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
#点击用户名输入框
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("夜舞天缘")
#点击密码输入框，输入密码
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("xxxxx")


#关闭浏览器
driver.quit()