# -*- coding: utf-8 -*-
# @File   : test_Wx
# @Time   : 2021/4/22 21:55 
# @Author : BLUE_JUZIUPUP
import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_Wx:

    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        #   desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['autoAcceptAlerts'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize('name,phone',[
        ['test003','10000000003'],
        ['test004', '10000000004'],

    ])
    def test_AddBrother(self,name,phone):
        """
             1、打开企业微信
             2、打开
             :return:
        """
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
        #                                                  'scrollIntoview(new Uiselector( ).text(“添加成员"").'
        #                                                  'instance(0));')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/au0').send_keys(name)
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/eq7').send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="设置部门"]').click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/fmw').click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/gur').click()
        time.sleep(3)
        self.driver.back()
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="{name}"]')



