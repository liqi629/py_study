# -*- coding: utf-8 -*-
# @Time     : 2019/5/22 8:58
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_09_alert弹窗.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#打开浏览器Chrome
driver = webdriver.Firefox()
#打开网址
driver.get("http://www.baidu.com")

#等待弹窗出现: 条件函数：EC.alert_is_present()，如果有，返回alert，没有返回Flase

WebDriverWait(driver,10).until(EC.alert_is_present())
#切换到alert
#alert = driver.switch_to_alert() #不使用了，有了更新的
alert = driver.switch_to.alert  #.laert有返回值，需要接收
#打印文本
print(alert.text)
#关闭弹窗——接受，ok
alert.accept()
#——否
alert.ddismiss()
#获取弹出框内容
alert.text()
#往弹出框输入内容
alert.send_keys()


#有时候，弹窗不一定出现，这时候就要进行判断

result = EC.alert_is_present(driver)
if result:
    print(alert.text)
    alert.accept()
else:
    print("未弹出")
# 判断弹窗是否出现
result = EC.alert_is_present()(driver)
if result:
    print (result.text)
    result.accept()
else:
    print ("alert 未弹出！")