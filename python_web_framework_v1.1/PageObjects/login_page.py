
from Common.BasePage import BasePage
from PageLocators.loginPage_locator import LoginPageLocator as loc

#继承BasePage
class LoginPage(BasePage):

    #登录操作
    def login(self,username,password):
        # 等待用户名输入框元素可见
        self.wait_eleVisible(loc.user_input)
        #输入用户名
        self.input_text(loc.user_input,username)
        #输入密码
        self.input_text(loc.passwd_input,password)
        #点击登录
        self.click_element(loc.login_button)

    #获取页面错误提示——登录表单区域
    def get_wrongMsg_uesr(self):
        #等待用户名错误提示元素可见,获取文本
        text = self.get_text(loc.from_erro_info_user)
        return text
    def get_wrongMsg_pwd(self):
        # 等待密码错误提示元素可见,获取文本
        text = self.get_text(loc.from_erro_info_pwd)
        return text
    #用户不存在
    def get_no_uesr(self):
        # 等待用户不存在错误提示元素可见,获取文本
        text = self.get_text(loc.from_erro_info_no_uesr)
        return text


