from selenium.webdriver.common.action_chains import ActionChains as AC
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
#点击设置
# driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]').click()
#1、实例化ActionChains类
ac=AC(driver)
#2、鼠标行为，最后调用perform来执行鼠标操作
ele=driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]')
ac.move_to_element(ele).click(ele).perform()
#等待高级搜索
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
#点击高级搜索
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()
