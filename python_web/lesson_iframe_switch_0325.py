from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

url='https://www.ketangpai.com/'
driver.get(url)
#全屏
driver.maximize_window()
#1:判断你要操作的元素，是否在iframe里面，如果在iframe里面 才需要切换
#2：切换  三种方式  下标  name   xpath
driver.switch_to.frame(4)
driver.switch_to.frame("login_fram_qq")
driver.switch_to.frame(driver.find_element_by_xpath("XXX"))

#操作iframe里面的html页面

#退出iframe  回到默认html页面
driver.switch_to.default_content()
#切换到上一级iframe  如果没有 就保留当前页面
driver.switch_to.parent_frame()

#方式二
#EC.frame_to_be_available_and_switch_to_it   # 方式1的三种参数都可以传 都可以传 函数自己判断
#等到iframe出现，并切换到iframe所在的html页面
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
driver.find_element_by_xpath("XXX")
