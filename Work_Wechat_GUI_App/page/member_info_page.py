# -*- coding: utf-8 -*-
# @File   : member_info_page
# @Time   : 2021/4/26 14:21 
# @Author : BLUE_JUZIUPUP
from appium.webdriver.common.mobileby import MobileBy

from Work_Wechat_GUI_App.page.BasePage import BasePage


class member_info_page(BasePage):
    def del_member(self):
        """

        :return:删除成员，返回管理通讯录页面
        """
        self.swipe_find("删除成员").click()
        self.find(MobileBy.XPATH,'//*[@text="确定"]').click()

        from Work_Wechat_GUI_App.page.manage_contact_page import manage_contact_page
        return manage_contact_page(self.driver)
