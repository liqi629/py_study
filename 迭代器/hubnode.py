# -*- coding: utf-8 -*-
# @Time     : 2019/9/9 11:16
# @Author   : l7
# @File     : hubnode.py
# @Software : PyCharm
from selenium import webdriver
chrome_capabilities ={
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}
browser = webdriver.Remote("http://172.16.7.18:5555/wd/hub", desired_capabilities=chrome_capabilities)
browser.get("http://www.163.com")
print(123)
browser.quit()