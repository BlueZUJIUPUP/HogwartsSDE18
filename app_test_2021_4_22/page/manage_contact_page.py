# -*- coding: utf-8 -*-
# @File   : manage_contact_page
# @Time   : 2021/4/26 14:18 
# @Author : BLUE_JUZIUPUP
import time

from appium.webdriver.common.mobileby import MobileBy

from app_test_2021_4_22.page.BasePage import BasePage


class manage_contact_page(BasePage):

    def goto_member_info_page(self):
        """

        :return: 跳转成员的个人信息页
        """
        ele=self.find(MobileBy.XPATH,'//android.widget.ListView/android.widget.RelativeLayout[1]//android.widget.TextView')
        name=ele.text
        ele.click()
        from app_test_2021_4_22.page.member_info_page import member_info_page
        return member_info_page(self.driver),name


    def assert_del_succeed(self,name):
        """

        :return: 在管理通讯录页面验证是否有该成员
        """
        """
        //*[@resource-id='com.tencent.wework:id/dyi']//android.widget.TextView
        /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]
        //*[@resource-id='com.tencent.wework:id/ftg']
        /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView
        """
        time.sleep(5)
        try:
            self.swipe_find(f"//*[@text='{name}']")
            return False
        except:
            return True