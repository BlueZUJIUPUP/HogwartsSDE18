# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/21 22:08
# @Author : BLUE_JUZIUPUP
import time

from selenium.webdriver.common.by import By

from Work_Wechat_GUI_Web.main.base_page import BasePage


class mian_list(BasePage):
    def dept_list(self):
        time.sleep(3)
        ele_list = self.driver.find_elements(By.CSS_SELECTOR,'.jstree-anchor')
        name_list = []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        return name_list




