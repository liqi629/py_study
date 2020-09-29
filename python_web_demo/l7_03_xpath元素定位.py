# -*- coding: utf-8 -*-
# @Time     : 2019/5/21 21:44
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_03_xpath元素定位.py
# @Software : PyCharm
from selenium import webdriver
#打开浏览器Chrome
driver = webdriver.Chrome()
#打开网址
driver.get("http://www.baidu.com")

#xpath元素定位
#绝对定位：以 / 开头，从根节点开始，严格按照顺序和位置来表达。不易维护，不使用这种方式
#相对定位：以 // 开头 ，不管元素的位置和顺序。在html页面当中，有没有匹配表达式的元素
#1、 //标签名[@属性名="属性值"]
   #文本定位   //标签名[text()="文本"]
   #包含定位   //标签名[contains(text(),"包含的文本")]    //标签名[contains(@属性="包含的属性值")]
#2、 逻辑运算    //标签名[@属性名="属性值" and @属性名="属性值"]   //标签名[@属性名="属性值" or @属性名="属性值"]
#3、 层级定位   元素本身属性不够唯一定位到自己，借助其比较近的祖先节点缩小查找范围
    #  //标签名[@属性名="属性值"]//标签名[@属性名="属性值"]
#轴定位
#
#找到父节点（parent::）——找父节点后面的（fllowing-sibling::）
# //标签名[text()="文本"]/parent::标签名/fllowing-sibling::标签名[@属性="属性值"]//标签名