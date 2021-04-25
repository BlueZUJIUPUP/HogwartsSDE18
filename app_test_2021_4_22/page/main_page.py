# -*- coding: utf-8 -*-
# @File   : main_page
# @Time   : 2021/4/25 16:42 
# @Author : BLUE_JUZIUPUP
from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.page.BasePage import BasePage
from app_test_2021_4_22.page.contact_page import contact_page


class main_page(BasePage):


    def goto_contact(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return contact_page(self.driver)