# -*- coding: utf-8 -*-
# @Time     : 2019/9/23 20:33
# @Author   : l7
# @File     : mythread.py
# @Software : PyCharm
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i)#name属性中保存的是当前线程的名字
            print(msg)

if __name__ == '__main__':
    t = MyThread()
    t.start()