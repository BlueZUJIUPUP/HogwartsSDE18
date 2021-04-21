# -*- coding:utf-8 -*
import pytest

from HogwartsSDE18.web_test_2021_4_18.main.contact import contact


class Test_case:
    def setup_class(self):
        self.main_page = contact()


    @pytest.mark.parametrize("dept_name",[['ceshi005'],['ceshi006']],ids=['ceshi005','ceshi006'])

    def test_add_member(self,dept_name):

        """
        :param dept_name: 1. 触发添加部门弹窗  2. 添加部门   3. 获取成员列表   4. 比对是否可以添加成功
        :return:
        """

        dept_name_list=self.main_page.contact().clickadd(dept_name).dept_list()
        print(dept_name)
        print(dept_name[0])
        dept_name = dept_name[0]
        assert dept_name in dept_name_list
