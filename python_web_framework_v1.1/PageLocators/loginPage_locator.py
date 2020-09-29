from selenium.webdriver.common.by import By
class LoginPageLocator:
    # 用户名输入框name="account"
    # user_input = (By.XPATH,'//input[@name="account"]')
    user_input = (By.NAME, "account")
    # 密码输入框
    passwd_input = (By.XPATH,'//input[@name="pass"]')
    # 登录按钮
    login_button = (By.XPATH,'//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')
    # 错误提示——登录——账号不能为空
    from_erro_info_user = (By.XPATH,"//p[@class='error-tips']")
    # 错误提示——登录——密码不能为空
    from_erro_info_pwd = (By.XPATH,"//*[@id='login']/div[2]/div[2]/p")
    # 用户不存在
    from_erro_info_no_uesr = (By.XPATH,'//p[@class="error-tips"]')