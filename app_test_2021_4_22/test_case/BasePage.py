# -*- coding: utf-8 -*-
# @File   : test_one
# @Time   : 2021/4/22 10:28
# @Author : BLUE_JUZIUPUP
from appium import webdriver


class Base_Page:

    def __init__(self,base_driver=None):
        if base_driver:
            self.driver=base_driver
        else:
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
