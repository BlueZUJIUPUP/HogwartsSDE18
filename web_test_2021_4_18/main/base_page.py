# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @File   : Open_Test
# @Time   : 2021/4/21 22:08
# @Author : BLUE_JUZIUPUP
import yaml
from selenium import webdriver

class BasePage:
    def __init__(self, base_driver=None):
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("../cookie/data.yaml",encoding="utf-8") as f:
                yaml_data = yaml.safe_load(f)
                print(yaml_data)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)
        else:
            self.driver = base_driver

    def find(self,by,element=None):
        """
             :param by: 定位方式 css, xpath, id
             :param element: 元素定位信息
             :return:
        """
        # 两种传入定位元素的方式，提高代码的兼容性
        # 如果传入的是元祖,那就只有一个参数
        if element == None:
            # 比如传入(By.ID, "username")
            # * 的作用是 解元祖 self.driver.find_element(*username) 等同于
            # self.driver.find_element(By.ID, "username")
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, element)
