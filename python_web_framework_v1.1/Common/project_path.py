
import os

#
# print(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
#
# print(os.path.realpath(__file__))
# print(os.path.split(os.path.realpath(__file__)))
# print(os.path.split(os.path.realpath(__file__))[0])
Project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置文件路径

case_config_path=os.path.join(Project_path,'config','case.config')


#测试用例的路径
test_case_path=os.path.join(Project_path,'test_data','api.xlsx')

#html报告的路径
report_path=os.path.join(Project_path,'test_result','reports','report.html')

#日志文件路径
log_path=os.path.join(Project_path,'test_result','logs','test_api.txt')
#截图文件路径
img_path=os.path.join(Project_path,'test_result','imgs')

#数据库配置文件路径
db_config_path=os.path.join(Project_path,'config','db.config')


if __name__ == '__main__':
    print(case_config_path)
    print(test_case_path)
    print(report_path)
    print(log_path)