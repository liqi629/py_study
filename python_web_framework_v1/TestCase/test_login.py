
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import Common_Datas as CD
from TestDatas import login_datas as ld
import ddt
@ddt.ddt
class TestLogin(unittest.TestCase):
    #整个类执行一次
    @classmethod
    def setUpClass(cls):
        print("整个测试类只执行一次的前置")
        pass

    @classmethod
    def tearDownClass(cls):
        print("整个测试类只执行一次的后置")
        pass
    #每个测试用例执行一次
    def setUp(self):
        print("测试类中每个测试用例都执行一次的前置")
        #打开浏览器，访问 课堂派登录页面
        self.driver=webdriver.Chrome()
        self.driver.get(CD.login_url)
        self.lp=LoginPage(self.driver)


    def tearDown(self):
        self.driver.quit()
    #正常场景：登录成功
    def test_login_success(self):
        #步骤  测试数据  18610430456   liqi_0827
        #登录页面——登录功能——输入用户名密码
        self.lp.login(ld.scuess_data["user"],ld.scuess_data["pwd"])
        #断言，根据登录成功后页面出现的特征元素，判断
        self.assertTrue(IndexPage(self.driver).is_user_link_exists())

    #异常场景：用户名为空
    @ddt.data(*ld.wrong_data)
    def test_login_nullUser(self,data):
        #步骤  测试数据  ""   liqi_0827  断言数据：账号不能为空
        self.lp.login(data["user"], data["pwd"])
        #断言
        self.assertEqual(data["check"],self.lp.get_wrongMsg_uesr())
    #异常场景：用户名、密码为空
    #
    # def test_login_nullUser_1(self):
    #     #步骤  测试数据  ""   liqi_0827  断言数据：账号不能为空
    #     self.lp.login("", "")
    #     #断言
    #     self.assertEqual("账号不能为空",self.lp.get_wrongMsg_uesr())
    #异常场景：密码为空
    def test_login_noPasswd(self):
        #步骤   测试数据  18610430456   ""
        LoginPage(self.driver).login("18610430456", "")
        #断言
        self.assertEqual("密码不能为空",self.lp.get_wrongMsg_pwd())
    #常场景：用户不存在
    def test_login_noUser(self):
        #步骤  测试数据
        self.lp.login(ld.wrong_user_format["user"], ld.wrong_user_format["pwd"])
        #断言
        self.assertEqual(ld.wrong_user_format["check"],self.lp.get_no_uesr())