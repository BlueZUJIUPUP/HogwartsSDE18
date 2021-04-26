# -*- coding: utf-8 -*-
# @File   : test_Wx
# @Time   : 2021/4/22 21:55 
# @Author : BLUE_JUZIUPUP
import logging
import sys
import time
import allure
import pytest

from app_test_2021_4_22.page.App import App
from app_test_2021_4_22.page.main_page import main_page
from app_test_2021_4_22.utils.get_func_name import get_fanc_name
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

        with allure.step("1、进入首页，2、进入通讯录，3、点击添加成员，进入添加成员模式选择页面，4、点击手动输入，5、进入成员的个人信息编辑页面"):
            succeed = self.main.goto_contact().goto_addmember().goto_edit_member_page()

        with allure.step("6、填写好成员资料，点击保存，7、验证是否添加成功"):
            result = succeed.edit_member(self.name, self.phone).assert_add_succeed()
            logging.info(f"{sys._getframe().f_code.co_name}用例结果为:"+str(result))
            assert result == True

    @allure.story("测试删除联系人联系人")
    @allure.severity('normal')
    def test_del_member(self):
        """
        删除联系人用例
        :return: 成功或失败
        """
        with allure.step("1、进入首页，2、进入通讯录，3、进入成员管理信息页面，4、进入成员的个人信息页面"):
            member_info = self.main.goto_contact().goto_manage_contact_page().goto_member_info_page()
            name = member_info[1]
        with allure.step(f"4、删除{name}成员信息"):
            del_member = member_info[0].del_member()

        with allure.step(f"验证是否在管理页还存在{name}成员信息"):
            result = del_member.assert_del_succeed(name)
            logging.info(f"{sys._getframe().f_code.co_name}用例结果为:" + str(result))
            logging.info(f"删除成员名字:{name}")
            assert result == True






