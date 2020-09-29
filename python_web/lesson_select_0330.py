from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
url='https://www.baidu.com/'
driver.get(url)
driver.maximize_window()#全屏
driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]').click()
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()
#等待select出现
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ft"]')))
#1:找到select元素
select_ele = driver.find_element_by_xpath('//select[@name="ft"]')
#2:初始化select类
s = Select(select_ele)
#3:选择值
#下标
s.select_by_index(2)
time.sleep(3)
#value属性
s.select_by_value("xls")
time.sleep(3)
#文本内容
s.select_by_visible_text("微软 Powerpoint (.ppt)")
time.sleep(3)