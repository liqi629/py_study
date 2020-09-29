# -*- coding: utf-8 -*-
# @Time     : 2019/4/19 16:49
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_login.py
# @Software : PyCharm
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import login_datas as ld
import pytest


@pytest.mark.usefixtures("init_driver")#整个套件setupClass
@pytest.mark.usefixtures("init_page")#每一个用例  setup
class TestLogin():
    #异常场景：用户名为空   用户密码都空
    def test_login_0_nullUser(self,data,init_driver):
        #步骤  测试数据
        init_driver[1].login(data["user"], data["pwd"])
        #断言
        assert data["check"]==init_driver[1].get_wrongMsg_uesr()

    #异常场景：密码为空
    def test_login_1_noPasswd(self,init_driver):
        #步骤   测试数据
        LoginPage(init_driver[0]).login("18120430454", "")
        #断言
        assert "密码不能为空"==init_driver[1].get_wrongMsg_pwd()
    #常场景：用户不存在
    def test_login_2_noUser(self,init_driver):
        #步骤  测试数据
        init_driver[1].login(ld.wrong_user_format["user"], ld.wrong_user_format["pwd"])
        #断言
        assert ld.wrong_user_format["check"]==init_driver[1].get_no_uesr()
    #正常场景：登录成功
    @pytest.mark.smoke
    def test_login_3_success(self,init_driver):#init_driver写入函数名称，代表返回值
        #步骤  测试数据
        #登录页面——登录功能——输入用户名密码
        init_driver[1].login(ld.scuess_data["user"],ld.scuess_data["pwd"])
        #断言，根据登录成功后页面出现的特征元素，判断
        assert IndexPage(init_driver[0]).is_user_link_exists()==True