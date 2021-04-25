# -*- coding: utf-8 -*-
# @File   : test_one
# @Time   : 2021/4/22 10:28
# @Author : BLUE_JUZIUPUP

import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


logging.basicConfig(level=logging.INFO)


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_by_scroll(self, text):
        logging.info("find_by_scroll")
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                        f'scrollIntoView(new UiSelector().text("{text}").instance(0));')


