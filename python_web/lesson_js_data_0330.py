
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
# driver.get('https://www.12306.cn/index/')
# #选择起始城市
# #选择终点城市
# #准备js语句  用来处理日期
# js = 'var a = document.getElementById("train_date");'\
#     'a.readOnly=false;'\
#     'a.value="2019-03-20";'
#
# #调用webdriver里面的函数执行   js
# driver.execute_script(js)
driver.get('https://www.baidu.com/')
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(text(),"-CSDN学院")]')))
time.sleep(0.5)
ele = driver.find_elements_by_xpath('//*[contains(text(),"-CSDN学院")]')
# 滚动条拉到底部
# js="var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
#滚动,聚焦元素，driver版本于浏览器版本不匹配，报错
driver.execute_script("arguments[0].scrollIntoView();",ele)
#移动元素到底端与当前窗口的底部对齐
# driver.execute_script("arguments[0].scrollIntoView(false);",ele)
# 移动元素到顶端与当前窗口的顶部对齐
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# #移动到页面底部
# driver.execute_script("windows.scrollTo(0,document,body.scrollHeight)")
# #移动到页面顶部
# driver.execute_script("windows.scrollTo(document,body.scrollHeight，0)")

