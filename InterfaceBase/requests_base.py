# -*- coding:utf8 -*-
"""
requests第一次封装
整个测试框架的基础
"""
import requests,json
from Public.log import LOG,logger

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}

@logger("requests封装文件：request_base.py")
class request(object):
    def __init__(self):
        # 自动加载浏览器请求头
       self.headers = headers

    #get请求方法,已调试成功
    def get(self,url,params):
        """
        :param url: 完整的请求url
        :param params: 完整的请求参数
        :return:返回值 “0” 代表接口可以连接，“1”代表无效接口连接
        """
        #将传入的接口参数，转换为json格式,可能无需转换，先调试
        params_json = json.dumps(params)
        try:
            '''
            也可以使用这种方式请求
             response = requests.request("GET", url, headers=self.headers, params=params)
            '''
            LOG.info("GET开始请求接口")
            response = requests.get(url, headers=self.headers, params=params_json)  #post方法请求接口
            LOG.info("GET接口请求成功，状态：%s" % response)
            response.encoding = "UTF-8"     #此处需要设置GET返回信息的字符集
            reponse_json = json.loads(response.text)
            LOG.info("接口返回json信息：%s"%reponse_json)
            return {'code':0,'return_result_json':reponse_json}
        except Exception as error:
            LOG.info('GET请求出错(位置requests的模块第一次封装，请求接口有误)，出错原因：%s'%error)
            return {'code':1,'return_result_json':'post请出错(位置requests的模块第一次封装，请求接口有误)，出错原因:%s'%error}

    #post请求方法,已调试成功
    def post(self,url,params):
        """
        :param url: 完整的请求url
        :param params: 完整的请求参数
        :return:返回值 “0” 代表接口可以连接，“1”代表无效接口连接
        """
        try:
            '''
            也可以使用这种方式请求
             response = requests.request("POST", url, headers=self.headers, params=params)
            '''
            LOG.info("POST开始请求接口")
            response = requests.post(url, headers=self.headers, params=params)  #post方法请求接口
            LOG.info("POST接口请求成功，状态：%s" % response)
            reponse_json = json.loads(response.text)
            LOG.info("接口返回json信息：%s"%reponse_json)
            return {'code':0,'return_result_json':reponse_json}
        except Exception as error:
            LOG.info('POST请求出错(位置requests的模块第一次封装，请求接口有误)，出错原因：%s'%error)
            return {'code':1,'return_result_json':'post请出错(位置requests的模块第一次封装，请求接口有误)，出错原因:%s'%error}

    # delete请求方法,已调试成功
    def delete(self, url, params):
        """
        :param url: 完整的请求url
        :param params: 完整的请求参数
        :return:返回值 “0” 代表接口可以连接，“1”代表无效接口连接
        """
        # 将传入的接口参数，转换为json格式,可能无需转换，先调试
        params_json = json.dumps(params)
        try:
            '''
            也可以使用这种方式请求
             response = requests.request("DELETE", url, headers=self.headers, params=params)
            '''
            LOG.info("DELETE开始请求接口")
            response = requests.delete(url, headers=self.headers, params=params_json)  # post方法请求接口
            LOG.info("DELETE接口请求成功，状态：%s" % response)
            reponse_json = json.loads(response.text)
            LOG.info("接口返回json信息：%s" % reponse_json)
            return {'code': 0, 'return_result_json': reponse_json}
        except Exception as error:
            LOG.info('DELETE请求出错(位置requests的模块第一次封装，请求接口有误)，出错原因：%s' % error)
            return {'code': 1, 'return_result_json': 'post请出错(位置requests的模块第一次封装，请求接口有误)，出错原因:%s' % error}



#未知原因：使用程序入口，无发打印信息
if __name__ == "__main__":  #不使用入口
    #post请求调试
    url = "http:/Account/Login"
    Interface_parameters = {"hnAccount": "16985652453", "hnPassword": "123456"}
    r = request()
    a = r.post(url,Interface_parameters)
    print("requests第一次封装")

