# -*- coding:utf-8 -*
from selenium.webdriver.common.by import By

from web_test_2021_4_18.main.Dept import dept
from web_test_2021_4_18.main.base_page import BasePage


class contact(BasePage):

    #跳转通信录
    def contact(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        return dept(self.driver)

