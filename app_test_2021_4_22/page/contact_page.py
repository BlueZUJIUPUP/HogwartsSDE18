# -*- coding: utf-8 -*-
# @File   : appcontact
# @Time   : 2021/4/23 10:01 
# @Author : BLUE_JUZIUPUP
import time

from app_test_2021_4_22.page.addmember_page import addmember_page
from app_test_2021_4_22.page.BasePage import BasePage


class contact_page(BasePage):
    def goto_addmember(self):
        """

        :return: 跳转添加成员页面
        """
        time.sleep(5)
        self.swipe_find("添加成员").click()
        return addmember_page(self.driver)
