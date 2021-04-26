# -*- coding: utf-8 -*-
# @File   : appcontact
# @Time   : 2021/4/23 10:01 
# @Author : BLUE_JUZIUPUP
import time

from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.page.addmember_page import addmember_page
from app_test_2021_4_22.page.BasePage import BasePage
from app_test_2021_4_22.page.manage_contact_page import manage_contact_page


class contact_page(BasePage):
    def goto_addmember(self):
        """

        :return: 跳转添加成员页面
        """
        self.swipe_find("添加成员").click()
        return addmember_page(self.driver)


    def goto_manage_contact_page(self):
        """

        :return: 跳转管理个人资料页面
        """
        self.find(MobileBy.ID,"com.tencent.wework:id/h8l").click()
        return manage_contact_page(self.driver)
