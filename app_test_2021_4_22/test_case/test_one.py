# -*- coding: utf-8 -*-
# @File   : test_one
# @Time   : 2021/4/22 10:28 
# @Author : BLUE_JUZIUPUP
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_suger():
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] =  'true'
        desired_caps['autoAcceptAlerts'] = 'true'
        #desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()
    def test_XXX(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name"][@text="阿里巴巴"]').click()
        jiage = self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text
        assert float(jiage) > 200.0
    def test_hudong(self):
        size=self.driver.get_window_size()
        time.sleep(3)
        x = size['width']
        y = size['height'] #100/5  #100/1.5
        TouchAction(driver=self.driver).press(x=x/2,y=y/1.5).wait(300).move_to(x=x/2,y=y/5).release().perform()
        '''
        使用uiautomator滚动
        当识别到某一元素后停止滚动
        self.driver.find_elements_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                         'scrollable(true).instance(0)).'
                                                         'scrollIntoview(new Uiselector( ).text(“雪盈证券"").'
                                                         'instance(0));' ).click()
         #1                                                
        '''


