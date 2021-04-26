# -*- coding: utf-8 -*-
# @File   : test_Wx
# @Time   : 2021/4/22 21:55 
# @Author : BLUE_JUZIUPUP
import logging
import time
import allure
import pytest

from app_test_2021_4_22.page.App import App
from app_test_2021_4_22.page.main_page import main_page
from app_test_2021_4_22.utils.get_random_info import get_random_info
logging.basicConfig(level=logging.INFO)


@allure.feature("添加联系人测试")
class Test_Wx:

    def setup_class(self):
        logging.info("开始测试_class")
        self.app = App()


    def setup(self):
        self.main = self.app.start().goto_main()
        logging.info("开始测试_func")

    def teardown(self):
        self.app.restart()
        logging.info("结束测试_func")

    def teardown_class(self):
        self.app.stop()
        logging.info("结束测试_class")

    @allure.story("测试添加联系人成功")
    @allure.severity('normal')
    def test_add_member(self):
        """
        添加联系人用例
        :return: 成功或失败
        """
        self.data = get_random_info()
        self.name = self.data.get_random_name()
        self.phone = self.data.get_random_phonenumber()
        logging.info(self.name+self.phone)
        succeed = self.main.goto_contact().goto_addmember().goto_edit_member_page().edit_member(self.name, self.phone).assert_add_succeed()
        logging.info(succeed)
        assert succeed == True

    @allure.story("测试删除联系人联系人")
    @allure.severity('normal')
    def test_del_member(self):
        del_member = self.main.goto_contact()






