# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/11 22:08
# @Author : BLUE_JUZIUPUP
import os

import pytest
import allure



if __name__ == '__main__':
    pytest.main(['-vs','-q','--alluredir','./report/result'])
    os.system("allure generate ./report/result/ -o ./report/html --clean")
    os.system("allure serve ./report/result/ -o ./report/html --clean")