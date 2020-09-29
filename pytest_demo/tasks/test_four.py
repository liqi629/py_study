# -*- coding: utf-8 -*-
# @Time     : 2019/8/16 16:34
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_four.py
# @Software : PyCharm
from collections import namedtuple
Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_asdict():
    t_task = Task('do something','okken',True,21)
    t_dict = t_task._asdict()
    expected = {'summary':'do something',
                'owner':'okken',
                'done':True,
                'id':21}
    assert t_dict==expected
def test_replace():
    t_before = Task('finsh book','brian',False)
    t_after = t_before._replace(id=10,done=True)
    t_expected = Task('finsh book','brian',True,10)
    assert t_after == t_expected