# -*- coding: utf-8 -*-
# @File   : test_execute_tools
# @Time   : 2021/7/30 22:56 
# @Author : BLUE_JUZIUPUP
from backend_test.utils.execute_tools import ExecuteTools
import pytest

class Test_execute:

    def test_get_jobs(self):
        print(ExecuteTools.get_jobs())

    def test_invoke(self):
        print(ExecuteTools.invoke())