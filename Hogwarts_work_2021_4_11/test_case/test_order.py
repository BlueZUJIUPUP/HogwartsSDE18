# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/11 22:08
# @Author : BLUE_JUZIUPUP
import pytest



@pytest.fixture(name="这是01用例")
def name():
    print("用例名字02")

@pytest.fixture(params=[1,2],ids=["01执行第一次","01执行第二次"])
def name_02():
    print("用例名字02")

class Test_order:


    def test_01(self,这是01用例):
        print("1")

    def test_02(self, name_02):
        print("02")

    def test_03(self):
        print("03")

    @pytest.mark.run(order=1)
    def test_04(self):
        print("04")


