# -*- coding: utf-8 -*-
# @File   : rewrite1
# @Time   : 2021/5/18 14:38 
# @Author : BLUE_JUZIUPUP
"""HTTP-specific events."""
import json

import mitmproxy.http


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        #
        new_url = "https://www.douban.com"
        self.mapremote(new_url,flow)



    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        file = "./response.josn"
        self.maplocal(file,flow)


    def maplocal(self,file,flow: mitmproxy.http.HTTPFlow):
        """
        写maplocad方法修改local
        :param file:
        :return:
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # 拿到响应数据信息
            # flow.response.text 是str 属性，所以如果要是操作
            # 这个对象的话，必须转换为python 字典的数据结构
            # 否则就只能使用和str 相关的 方法
            with open(file=file,mode="r",encoding="utf-8")as f:
                a=f.read()
                flow.response.text = a


    def mapremote(self, new_url,flow: mitmproxy.http.HTTPFlow):
        """
        写mapremote方法修改
        :param file:
        :return:
        """
        old_url = flow.request.pretty_url
        if "https://www.baidu.com" in old_url:
            flow.request.url = new_url



addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    #使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
