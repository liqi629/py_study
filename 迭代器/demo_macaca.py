# -*- coding: utf-8 -*-
# @Time     : 2019/8/27 17:44
# @Author   : l7
# @File     : demo_macaca.py
# @Software : PyCharm
# -*- coding: utf-8 -*-
# @Time     : 2019/8/27 17:33
# @Author   : l7
# @File     : demo_macaca.py
# @Software : PyCharm
# 首先启动macaca server
# C:\Users\mrl>macaca server --verbose
# C:\Users\mrl\AppData\Roaming\npm\node_modules\macaca-chrome\node_modules\
# macaca-chromedriver\exec,目录下的chromedriver更换成语浏览器匹配的版本，并重命名为2.45，否则程序自动下载一个
from macaca import WebDriver
desired_caps = {
    'browserName': 'Chrome',  # Electon, Safari(iOS).
    'platformName': 'Desktop',  # iOS, Android.
    # 'platformVersion': '*',
    'autoAcceptAlerts': True
}
server_url = 'http://confluence.yoyosys.com.cn:8090'
driver = WebDriver(desired_caps)
driver.init()
# driver.maximize_window()
driver.get(server_url)
driver.wait_for_element('xpath','//input[@name="os_username"]').send_keys("li.qi")
driver.wait_for_element('id','os_password').send_keys("yoyo1234567")
driver.wait_for_element('id','loginButton').click()
driver.close()
#

#
# import unittest
# from macaca import WebDriver
# from time import sleep
#
#
# desired_caps = {
#     'platformName': 'Desktop',  #// iOS, Android, Desktop
#     'browserName': 'Chrome',    #// Chrome, Electron
#     'autoAcceptAlerts': True
# }
#
# # 对应Macaca服务的ip和端口号。
# server_url = {
#     'hostname': '127.0.0.1',
#     'port': 3456
# }
#
# class MacacaTest(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = WebDriver(desired_caps, server_url)
#         cls.driver.init()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#     def test_get_url(self):
#         self.driver.get('https://www.baidu.com')
#         self.assertEqual(self.driver.title, '百度一下，你就知道')
#
#     def test_search_macaca(self):
#         self.driver.element_by_id("kw").send_keys("macaca")
#         self.driver.element_by_id("su").click()
#         sleep(2)
#         title = self.driver.title
#         self.assertTrue('macaca',title)
#
#
# if __name__ == '__main__':
#     unittest.main()