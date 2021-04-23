# -*- coding: utf-8 -*-
# @File   : test_AddBrother
# @Time   : 2021/4/22 22:52 
# @Author : BLUE_JUZIUPUP
import time

from appium.webdriver.common.mobileby import MobileBy

from HogwartsSDE18.app_test_2021_4_22.test_case.BasePage import Base_Page


class AddBrother(Base_Page):


    def addBrother(self,name,phone):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/au0').send_keys(name)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/eq7').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="设置部门"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fmw').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gur').click()


        ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").is_displayed()
        print(ele)
        try:
            if ele == True:
                self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
                self.driver.back()
                print('手机已存在于通讯录返回')
                self.driver.find_element(MobileBy.XPATH,"//*[@text='取消']").click()
                self.driver.back()
                return True
            else:
                self.driver.back()
                print('正常返回')
                self.driver.find_element(MobileBy.XPATH, f'//*[@text="{name}"]')
                return True
        except:
            return False

