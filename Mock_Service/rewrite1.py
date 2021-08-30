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
        print("-" * 30)
        print(flow.request.url)
        print(flow.request.pretty_url)
        print("-"*30)
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # 拿到响应数据信息
            # flow.response.text 是str 属性，所以如果要是操作
            # 这个对象的话，必须转换为python 字典的数据结构
            # 否则就只能使用和str 相关的 方法
            print("*" * 30)
            print(flow.response.text)
            print("*" * 30)
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "test"
            data["data"]["items"][1]["quote"]["name"] = "test"
            flow.response.text = json.dumps(data)


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    #使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])