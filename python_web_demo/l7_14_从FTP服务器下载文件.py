# -*- coding: utf-8 -*-
# @Time     : 2019/6/5 17:36
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : l7_14_从FTP服务器下载文件.py
# @Software : PyCharm
import paramiko

# 实例化一个transport对象
transport = paramiko.Transport(('172.16.12.28', 22))
# 建立连接
transport.connect(username='root', password='yoyosys')

# 实例化一个 sftp对象,指定连接的通道
sftp = paramiko.SFTPClient.from_transport(transport)
# LocalFile.txt 上传至服务器 /home/fishman/test/remote.txt
# sftp.put('LocalFile.txt', '/home/fishman/test/remote.txt')
# 将LinuxFile.txt 下载到本地 fromlinux.txt文件中
sftp.get('/user/liqitest/auto_text_01', 'D:\YOYO\\auto_web_echo_v1\TestDatas/local_auto_text_01')
transport.close()