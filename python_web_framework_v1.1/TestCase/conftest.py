import pytest
from TestDatas import Common_Datas as CD
from selenium import webdriver
from PageObjects.login_page import LoginPage
driver=None
@pytest.fixture()
def init_page():
    global driver
    #前置
    print("============测试类中每个测试用例都执行一次的前置============")
    yield
    #后置
    print("============测试类中每个测试用例都执行一次的后置============")
    driver.get(CD.login_url)
#指明作用域
@pytest.fixture(scope="class")
def init_driver():
    global driver
    print("============整个测试类只执行一次的前置============")
    # 打开浏览器
    driver = webdriver.Chrome()
    # 设置全屏
    driver.maximize_window()
    lp = LoginPage(driver)
    # 打开目标网页
    driver.get(CD.login_url)
    yield [driver,lp]#关键字隔开前置、后置    后面空格[返回值]
    #后置
    print("============整个测试类只执行一次的后置============")
    driver.quit()

@pytest.fixture(scope="session",autouse=True)
def mySession():
    print ("============我是session级别的会话=====开始=====")
    yield
    print ("============我是session级别的会话=====结束=====")