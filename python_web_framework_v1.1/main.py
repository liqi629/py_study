# -*- coding: utf-8 -*-
# @Time     : 2019/4/19 16:51
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : main.py
# @Software : PyCharm
from Common import project_path
from Common.send_email import sendEmail
import pytest


pytest.main(["--html=test_result/reports/report.html","--junitxml=test_result/reports/report.xml"])
#执行完毕之后，发送测试报告
sendEmail().send_email('liqi_629@163.com',project_path.report_path)