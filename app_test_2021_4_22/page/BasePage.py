# -*- coding: utf-8 -*-
# @File   : test_one
# @Time   : 2021/4/22 10:28
# @Author : BLUE_JUZIUPUP

import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def swipe_find(self, text, num=5):
        """
        滑动查找元素的方法
        :param text: 滑动查找元素的文本信息
        :param num: 滑动查找的次数
        :return: 返回一个找出的元素
        """
        self.driver.implicitly_wait(1)
        for i in range(0, num):
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except NoSuchElementException:
                print("未找到，滑动")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']
                # 'width', 'height'
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000  # 滑动速度
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")

