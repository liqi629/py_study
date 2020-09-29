# -*- coding: utf-8 -*-
# @Time     : 2019/12/2515:58
# @Author   : l7
# @File     : demo.py
# @Software : PyCharm

import pytest
import allure
class TestDemo:

    def test_timedistance_v0(self):
        assert 1==1
        print("hahha")
# @pytest.mark.parametrize("a,b,expected", testdata)
# def test_timedistance_v0(a, b, expected):
#     diff = a - b
#     assert diff == expected
#
#
# @pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
# def test_timedistance_v1(a, b, expected):
#     diff = a - b
#     print(diff)
#     assert diff == expected
# # @pytest.mark.parametrize("a,b,c", testdata1,ids=['1'])
# # def test_from(a,b,c):
# #     test_f=a+b
# #     assert test_f==c
# @pytest.mark.parametrize("test_input,expected",[("3+5",8),("3+9",12),("3*5",8),])
# def test_evel(test_input,expected):
#     assert  eval(test_input)==expected
if __name__ == '__main__':

    pytest.main(['-s', '-q', '--alluredir', './report/html']) #执行改目录下的所有测试脚本且生成测试报告，生成报告肯定是非易懂的所以后面用到allure
