# -*- coding: utf-8 -*-
# @File   : App
# @Time   : 2021/4/23 14:47 
# @Author : BLUE_JUZIUPUP
import logging

from appium import webdriver

from app_test_2021_4_22.page.BasePage import BasePage
from app_test_2021_4_22.page.main_page import main_page

logging.basicConfig(level=logging.INFO)

class App(BasePage):


    def start(self):
        if self.driver == None:
            print("driver等于空，初始化 driver")
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '7.1.2'
            desired_caps['deviceName'] = '127.0.0.1:62001'
            # desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            desired_caps['unicodeKeyboard'] = 'true'
            desired_caps['resetKeyboard'] = 'true'
            desired_caps['autoAcceptAlerts'] = 'true'
            # desired_caps['dontStopAppOnReset'] = 'true'
            desired_caps['noReset'] = 'true'
            desired_caps['skipDeviceInitialization'] = True
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(10)

        else:
            print("driver等于空，复用 driver")
            # start_activity 启动页面，可以运行过程中启动其它app或者当前app的其它页面
            # self.driver.start_activity(package_name, activityname)
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):

        return main_page(self.driver)

