from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#打开一个指定的浏览器
driver = webdriver.Chrome()
url='https://www.baidu.com/'
driver.get(url)
#全屏
driver.maximize_window()

#点击登录的链接
driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_login"]').click()
#固定等待sleep
time.sleep(2)
#点击用户名密码登录的方式
locator = (By.ID,"TANGRAM__PSP_10__footerULoginBtn")
#显性等待 ，默认轮询周期0.5
# presence_of_element_located:元素存在
#visibility_of_element_located:元素可见
#element_to_be_clickable:元素可点击


WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))


driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
locator=(By.ID,"TANGRAM__PSP_10__userName")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('11111111')
time.sleep(2)
#关闭当前窗口
driver.close()

#关闭整个浏览器
driver.quit()