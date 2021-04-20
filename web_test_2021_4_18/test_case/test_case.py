# -*- coding:utf-8 -*
from web_test_2021_4_18.main.contact import contact


class Test_case:
    def setup_class(self):
        self.main_page = contact()

    def test_add_member(self):

    # 1. 跳转到添加成员页面  2. 添加成员   3. 获取成员列表
        dept_name_list=self.main_page.contact().clickadd().dept_list()
        name = "ceshi03"
        assert name in dept_name_list
