from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

#等待 import time  time.sleep(2)

#显性等待
#1：明确等到某个条件满足之后，再去执行下一步操作
#2：程序每隔X秒查看一次，如果条件成立则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出Exception

#3：WebDriverWait类：显性等待
WebDriverWait(driver,10).until()
EC.invisibility_of_element_located((By.ID,))



#隐性等待
#1： 代码开头设定  代码之后的生效 代码之前不生效
#2： 如果设定时间内元素出现  就执行之后的代码
#3：可以等待元素  但是弹窗不能 aleter
driver.implicitly_wait(30)

#显性等待优先    sleep 一定执行

#元素的四大操作   click  sendkeys   get_attribute    .text