from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

url='https://www.baidu.com/'
driver.get(url)
#全屏
driver.maximize_window()

#找到触发alert的操作
driver.find_element_by_xpath("XX").click()
#等待弹窗(js弹窗)出现
WebDriverWait(driver,20).until(EC.alert_is_present())

#弹出了alert 切换进alert
alert = driver.switch_to.alert
#打印他的文本
print(alert.text)
#关闭弹窗-接受,ok
alert.accept()

