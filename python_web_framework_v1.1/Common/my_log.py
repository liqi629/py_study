#接口自动化使用的log
#日志：记录 系统的操作  记录代码的运行
#log
#日志分为5个级别：debug  info  warning  error  critical（crash）
#从左往右  级别依次加重
#logging Python 日志模块系统  可以直接拿来用
#收集日志：收集器  会有一个名字  默认顶级收集器：root
# 默认只收集warning（包含）以上级别的信息
#输出日志：输出控制台

import logging
from Common import project_path
class MyLog:
    #定义一个属于自己的日志收集器
    def my_log(self,level,msg):
        my_logger=logging.getLogger("python10")
        my_logger.setLevel("DEBUG")#设置收集级别

        #创造一个专属输出渠道  过滤 和排版
        #格式：
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')

        ch=logging.StreamHandler()#创建一个实例   输出到控制台
        ch.setLevel("DEBUG")#设置输出级别  大写
        ch.setFormatter(formatter)

        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')#输出到指定文件
        fh.setLevel("DEBUG")#设置输出级别  大写
        fh.setFormatter(formatter)

        # 对接起来  给日志收集器添加一个渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITIAL':
            my_logger.critical(msg)
        #渠道记得移除  否则 日志输出会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log("DEBUG",msg)
    def info(self,msg):
        self.my_log("INFO",msg)
    def warning(self,msg):
        self.my_log("WARNING",msg)
    def error(self,msg):
        self.my_log("ERROR",msg)
    def critical(self,msg):
        self.my_log("CRITICAL",msg)
if __name__=='__main__':
    my_logger=MyLog()



    my_logger.my_log("DEBUG","没有见过的日志")
    my_logger.info("不要慌")
    my_logger.warning("你也没见过")
    my_logger.error("有老夫")
    my_logger.critical("要崩溃啦")

#升级点：
#日志级别 logger name  输出格式  可不可以做成可配置