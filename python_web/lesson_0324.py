
from selenium import webdriver

#打开一个指定的浏览器
driver = webdriver.Chrome()
url='https://www.baidu.com/'
driver.get(url)
#1:id定位
ele = driver.find_element_by_id('kw')
#2:class_name定位
driver.find_element_by_class_name('s_ipt')
#如果找页面中所有的匹配元素
eles = driver.find_elements_by_class_name('s_ipt')
#3:tag
driver.find_elements_by_tag_name()
#4:name
driver.find_element_by_name()
#5/6: 针对a元素  2种查找方式  link  全部一致  模糊
driver.find_elements_by_link_text()
driver.find_elements_by_partial_link_text()#模糊
#8:css_selector

#7:xpath  重点使用
#绝对定位   相对定位
#相对
#1 //标签名[@属性名=属性值]
#2  逻辑   多个属性//标签名[@属性名=属性值and@属性名=属性值] 也可or
#3 层级//标签名[@属性名=属性值]/标签名[@属性名=属性值]                分层/和//  都可以
#contains()，该函数可以用来匹配包含某部分内容，如//div[contains(@id,‘layui-layer‘)]，表示id属性内容包含layui-layer的div元素

#text()，该函数可以用来匹配元素中间的文本，特别适合超链接，按钮。如//*[text()=‘White list‘]，表示文本为White list的任何元素

