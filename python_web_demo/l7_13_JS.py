# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 23:05
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_13_JS.py
# @Software : PyCharm
from selenium import webdriver
#时间控件，选日期。不能直接输入，需要使用js
#准备js语句
js = 'var a = var b = document.getElementById("id"):'\
    'a.readOnly = false:'\
    'a.value = "2019-51-20:'

driver = webdriver.Firefox()
#调用webdriver里面的方法执行js
driver.execute(js)


#滚动条
