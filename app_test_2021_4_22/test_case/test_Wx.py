# -*- coding: utf-8 -*-
# @File   : test_Wx
# @Time   : 2021/4/22 21:55 
# @Author : BLUE_JUZIUPUP
import time
import allure
import pytest

from app_test_2021_4_22.page.App import App
from app_test_2021_4_22.page.main_page import main_page


@allure.feature("添加联系人测试")
class Test_Wx:

    def setup_class(self):
        print("kaishi_class")
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()
        print("kaishi_func")

    def teardown(self):
        self.app.restart()
        print("jiesu_func")

    def teardown_class(self):
        self.app.stop()
        print("jiesu_class")

    def test_add_member(self):
        self.main.goto_contact().goto_addmember().goto_edit_member_page().edit_member().find_toast()


    @allure.story("添加联系人成功")
    @allure.severity('normal')
    @pytest.mark.parametrize('name,phone',[
        ['test004','10000000004'],
        #['test003', '10000000003']
    ])
    def test_add_member01(self, get_init, name, phone):
        """

        :param get_init: 初始函数
        :param name: 添加的成员的名字
        :param phone: 添加的成员的手机号
        :return:
        """
        # with allure.step("进入添加联系人页面"):
        #     self.res = home_page().go_contact().appcontact()
        #
        # with allure.step("输入联系人信息并保存"):
        #     self.contact_name = self.res.addBrother(name,phone).find_by_scroll(name).text
        #
        # with allure.step("验证是否添加成功"):
        #     assert self.contact_name == name
        pass






