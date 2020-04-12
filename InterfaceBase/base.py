# -*- coding: utf-8 -*-
"""
request第二次封装，引用“from InterfaceBase.requests_base import request”
"""

from InterfaceBase.requests_base import request
request = request()

class RequestApi(object):

    def __init__(self, url, params, method):
        self.url = url    #接口请求url
        # self.key = key    #接口请求key值
        self.param = params    #接口连接方式
        self.rehquest_metod = method     #接口请求方式，post、get、put、delete

    def testapi(self):
        if self.rehquest_metod == "POST":
            # print("POST")
            self.response = request.post(self.url, self.param)
        elif self.rehquest_metod == "GET":
            self.response = request.get(url=self.url, params=self.param)
        elif self.rehquest_metod == "DELETE":
            self.response = request.delete(url=self.url, params=self.param)
        return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data

if __name__ == "__main__":

    api = RequestApi(url="http://XXX/Account/Login", params={"hnAccount":"1158984565456","hnPassword":"123456"}, method="POST")
    # api.testapi()
    api_json = api.getJson()
    print(api_json)
    print("第二次请求接口")