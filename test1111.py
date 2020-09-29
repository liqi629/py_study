# -*- coding: utf-8 -*-
# @Time     : 2019/12/318:12
# @Author   : l7
# @File     : test1111.py
# @Software : PyCharm
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Console1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_console1(self):
        driver = self.driver
        driver.get("http://172.16.161.127:8080/login?redirect=%2Fmain")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div/section").click()
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div/section/main/div/div[2]/section/div/div/form/div[2]/div/div/textarea").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div/section/main/div/div[2]/section/div/div/form/div[2]/div/div/textarea").clear()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div/section/main/div/div[2]/section/div/div/form/div[2]/div/div/textarea").send_keys(
            "172.16.161.129")
        driver.find_element_by_xpath("//input[@type='password']").click()
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("yoyosys@2019")
        driver.find_element_by_xpath("(//input[@type='password'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='password'])[2]").send_keys("yoyosys@2019")
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
