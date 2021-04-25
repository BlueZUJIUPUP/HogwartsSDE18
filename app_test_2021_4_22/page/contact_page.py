# -*- coding: utf-8 -*-
# @File   : appcontact
# @Time   : 2021/4/23 10:01 
# @Author : BLUE_JUZIUPUP
from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.page.addmember_page import addmember_page
from app_test_2021_4_22.page.BasePage import BasePage


class contact_page(BasePage):
    def goto_addmember(self):
        """

        :return: 跳转添加成员页面
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return addmember_page()
