# -*- coding: utf-8 -*-
# @File   : get_func_name
# @Time   : 2021/4/26 14:48 
# @Author : BLUE_JUZIUPUP
import sys


def get_fanc_name(result):

   return (f"{sys._getframe().f_code.co_name}用例结果为:"+str(result))
