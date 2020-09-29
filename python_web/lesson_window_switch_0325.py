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
#进行搜索操作
driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id('su').click()
#获取当前所有窗口
windows=driver.window_handles
print("目前所有窗口",windows)
#点击百度贴吧链接
locator = (By.XPATH,'//div[@tpl="tieba_general"]')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
driver.find_element_by_xpath('//div[@tpl="tieba_general"]//a[text()="吧_百度贴吧"]').click()
#等待新窗口的出现
WebDriverWait(driver).until(EC.new_window_is_opened(windows))#判断新窗口是否打开
#切换浏览器窗口

#打印当前窗口
cur_window=driver.current_window_handle
print(cur_window)

#切换到最新打开的窗口
driver.switch_to.window(windows[-1])
#打印切换之后的窗口
print("切换之后的窗口",driver.current_window_handle)

#切回之前的窗口
driver.switch_to.window(windows[0])

time.sleep(2)
#关闭当前窗口
driver.close()

#关闭整个浏览器
driver.quit()