from web_test_2021_4_18.main.base_page import BasePage
from selenium.webdriver.common.by import By


class mian_list(BasePage):
    def dept_list(self):
        ele_list = self.driver.find_elements(By.CSS_SELECTOR,'.jstree-anchor')
        print(ele_list)
        name_list = []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list




