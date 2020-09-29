from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage:
    #用户名输入框
    user_input='//input[@name="account"]'
    # 密码输入框
    passwd_input = '//input[@name="pass"]'
    # 登录按钮
    login_button = '//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]'
    #错误提示——登录——账号不能为空
    from_erro_info_user="//p[@class='error-tips']"
    #错误提示——登录——密码不能为空
    from_erro_info_pwd="//*[@id='login']/div[2]/div[2]/p"
    #用户不存在
    from_erro_info_no_uesr='//p[@class="error-tips"]'
    def __init__(self,driver):#必须外部传入driver  同一个driver经历多个页面
        self.driver=driver
    #登录操作
    def login(self,username,password):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,self.user_input)))
        self.driver.find_element_by_xpath(self.user_input).send_keys(username)#输入用户名
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.passwd_input)))
        self.driver.find_element_by_xpath(self.passwd_input).send_keys(password)  # 输入密码
        self.driver.find_element_by_xpath(self.login_button).click()#点击登录

    #获取页面错误提示——登录表单区域
    def get_wrongMsg_uesr(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,self.from_erro_info_user)))
        return self.driver.find_element_by_xpath(self.from_erro_info_user).text
    def get_wrongMsg_pwd(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,self.from_erro_info_pwd)))
        return self.driver.find_element_by_xpath(self.from_erro_info_pwd).text
    #用户不存在
    def get_no_uesr(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.from_erro_info_no_uesr)))
        return self.driver.find_element_by_xpath(self.from_erro_info_no_uesr).text
