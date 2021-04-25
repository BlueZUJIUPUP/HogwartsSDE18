# -*- coding: utf-8 -*-
# @File   : home_page
# @Time   : 2021/4/23 9:50 
# @Author : BLUE_JUZIUPUP
from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.page.BasePage import BasePage
from app_test_2021_4_22.page.contact_page import app_contact


class home_page(BasePage):
    def go_contact(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return app_contact(self.driver)




