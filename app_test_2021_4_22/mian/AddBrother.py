# -*- coding: utf-8 -*-
# @File   : test_AddBrother
# @Time   : 2021/4/22 22:52 
# @Author : BLUE_JUZIUPUP
import time

from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.mian.BasePage import BasePage


class AddBrother(BasePage):


    def addBrother(self,name,phone):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/au0').send_keys(name)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/eq7').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="设置部门"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fmw').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gur').click()
        time.sleep(2)
        self.driver.back()
        return True

