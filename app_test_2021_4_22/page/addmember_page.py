# -*- coding: utf-8 -*-
# @File   : test_AddBrother
# @Time   : 2021/4/22 22:52 
# @Author : BLUE_JUZIUPUP
import time

from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.page.BasePage import BasePage
from app_test_2021_4_22.page.edit_member_page import edit_member_page


class addmember_page(BasePage):

    def goto_edit_member_page(self):
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return edit_member_page(self.driver)

    def back_contact(self):

        from app_test_2021_4_22.page.contact_page import contact_page
        return contact_page(self.driver)

    def assert_add_succeed(self):
        return self.find_toast(MobileBy.XPATH, '//*[@text="添加成功"]')




