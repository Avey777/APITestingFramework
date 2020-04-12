# -*- coding: utf-8 -*-
"""
接口封装文件
"""
import requests
from config.config import *
# url = "http://cpright.xinhua-news.cn/api/match/image/getjson"
#
# querystring = {"category":"image","offset":"0","limit":"30","sourceId":"0","metaTitle":"","metaId":"0","classify":"unclassify","startTime":"","endTime":"","createStart":"","createEnd":"","sourceType":"","isTracking":"true","metaGroup":"","companyId":"0","lastDays":"1","author":""}
#
# headers = {
#     'cache-control': "no-cache",
#     'postman-token': "e97a99b0-424b-b2a5-7602-22cd50223c15"
#     }
#
# response = requests.request("POST", url, headers=headers, params=querystring)

################################
url = "http://www.shangzhan168.cn/Account/Login"
# url = "http://xxxXXXsys/login"
# querystring = {"username":"16895654212","password":"123456"}
headers = {
    'cache-control': "no-cache"
    }
querystring = {"hnAccount":"15020579681","hnPassword":"123456"}
#Post接口调用
response = requests.request("POST", url,headers=headers, params=querystring)
print(response.json())
print(response.text)
print(response.cookies)
print(response.apparent_encoding)
print(response.headers)
print(response.content)
