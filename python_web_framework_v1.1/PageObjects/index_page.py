from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageLocators.indexPage_locator import IndexPage as loc
from selenium import webdriver

class IndexPage:

    def __init__(self,driver):
        self.driver=driver

    #判断用户昵称元素是否存在
    def is_user_link_exists(self):
        """
        如果存在返回True，如果不存在返回False
        :return: 
        """
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc.user_link))
            return True
        except:
            return False
