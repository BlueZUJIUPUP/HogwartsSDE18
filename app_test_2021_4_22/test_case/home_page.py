# -*- coding: utf-8 -*-
# @File   : home_page
# @Time   : 2021/4/23 9:50 
# @Author : BLUE_JUZIUPUP
from appium.webdriver.common.mobileby import MobileBy

from HogwartsSDE18.app_test_2021_4_22.test_case.BasePage import Base_Page
from HogwartsSDE18.app_test_2021_4_22.test_case.appcontact import app_contact


class home_page(Base_Page):
    def go_contact(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return app_contact(self.driver)

    def quit(self):
        self.driver.quit()


