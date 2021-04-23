# -*- coding: utf-8 -*-
# @File   : appcontact
# @Time   : 2021/4/23 10:01 
# @Author : BLUE_JUZIUPUP
from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.mian.AddBrother import AddBrother
from app_test_2021_4_22.mian.BasePage import BasePage


class app_contact(BasePage):
    def appcontact(self):
        """

        :return: 跳转添加成员页面
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return AddBrother(self.driver)
