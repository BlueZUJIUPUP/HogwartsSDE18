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
        self.find(MobileBy.XPATH, '//*[contains(@text,"姓名") ]/../android.widget.EditText').send_keys(name)
        self.find(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phone)
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

        from app_test_2021_4_22.page.addmember_page import addmember_page
        return addmember_page(self.driver)
