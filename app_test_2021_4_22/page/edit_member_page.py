# -*- coding: utf-8 -*-
# @File   : edit_member_page
# @Time   : 2021/4/25 16:52 
# @Author : BLUE_JUZIUPUP
from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.page.BasePage import BasePage


class edit_member_page(BasePage):
    def edit_member(self,name,phone):
        """
        编辑成员页面
        :param name: 成员名称
        :param phone: 成员手机号
        :return: 点击保存后跳转回添加成员选择方式页面
        """
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/au0').send_keys(name)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/eq7').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="设置部门"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fmw').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gur').click()

        from app_test_2021_4_22.page.addmember_page import addmember_page
        return addmember_page()
