# -*- coding: utf-8 -*-
# @Time     : 2019/7/23 9:35
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : temple.py
# @Software : PyCharm
import mock
def zhifu():
    '''假设这里是一个支付的功能,未开发完
    支付成功返回：{"result": "success", "reason":"null"}
    支付失败返回：{"result": "fail", "reason":"余额不足"}
    reason返回失败原因
    '''
    pass

def zhifu_statues():
    '''根据支付的结果success or fail，判断跳转到对应页面'''
    result = zhifu()
    print(result)
    try:
        if result["result"] == "success":
            return "支付成功"
        elif result["result"] == "fail":
            print("失败原因：%s" % result["reason"])
            return "支付失败"
        else:
            return "未知错误异常"
    except:
        return "Error, 服务端返回异常!"