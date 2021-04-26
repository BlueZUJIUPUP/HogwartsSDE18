# -*- coding: utf-8 -*-
# @File   : get_random_info
# @Time   : 2021/4/25 22:32 
# @Author : BLUE_JUZIUPUP

from faker import Faker


class get_random_info():
    def __init__(self):
        self.fake_data = Faker('zh_CN')

    def get_random_name(self):
        """
        获取随机的中文名名称
        :return:
        """
        random_name = self.fake_data.name()
        print(random_name)
        return random_name

    def get_random_phonenumber(self):
        """
        获取随机的11位的手机号
        :return:
        """
        random_phonenumber = self.fake_data.phone_number()
        print(random_phonenumber)
        return random_phonenumber


if __name__ == '__main__':
    a = get_random_info()
    print(a.get_random_name())
    print(a.get_random_phonenumber())