# -*- coding: utf-8 -*-
# @File   : test
# @Time   : 2021/4/8 22:50 
# @Author : BLUE_JUZIUPUP
from Open_Test import open_test


test_case = open_test()[0]
print(list(test_case))
test_add_list=[]
for k in test_case:
    test_add_list.append(test_case[k])
print("-------")
#test_add_list=[]
# nm=['1','2','3','4','5','6']
# for test_add_list in nm:
#     test_add_list.append(test_add_list)
# for test_add_list in test_case:
#     test_add_list.append(test_add_list)
#print(test_add_list)
print("++++++++")
#test_add_list = test_case['add_int']
#test_sub_list = test_case['sub_int']
#print(test_add_list)