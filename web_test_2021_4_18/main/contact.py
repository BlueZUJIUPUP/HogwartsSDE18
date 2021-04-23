# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/21 22:08
# @Author : BLUE_JUZIUPUP
from selenium.webdriver.common.by import By

from HogwartsSDE18.web_test_2021_4_18.main.Dept import dept
from HogwartsSDE18.web_test_2021_4_18.main.base_page import BasePage


class contact(BasePage):

    #跳转通信录
    def contact(self):
        self.find(By.CSS_SELECTOR,'#menu_contacts').click()
        return dept(self.driver)

