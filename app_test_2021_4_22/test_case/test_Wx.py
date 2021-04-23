# -*- coding: utf-8 -*-
# @File   : test_Wx
# @Time   : 2021/4/22 21:55 
# @Author : BLUE_JUZIUPUP
import time

import allure
import pytest

from HogwartsSDE18.app_test_2021_4_22.test_case.home_page import home_page


class Test_Wx:

    def setup_class(self):
        print("kaishi")
    def teardown_class(self):
        main_page = home_page()
        yield main_page
        main_page.quit()
        print("退出")

    @allure.title("测试添加成员")
    @pytest.mark.parametrize('name,phone',[
        ['test001','10000000001'],
        ['test005', '10000000005']

    ])
    def test_add_member(self, name, phone):
        self.res = home_page().go_contact().appcontact().addBrother(name,phone)
        assert self.res






