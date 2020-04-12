# -*- coding: utf-8 -*-
"""
测试用例设计
"""
import json
import os
from InterfaceBase.base import RequestApi
from Public.assertion import assert_in
from Public.get_excel import dataParsing
from Public.log import logger, LOG
from config.config import *

# filepath = os.path.dirname(os.getcwd())+'\\data\\case.xlsx'
filepath = os.getcwd()+'\\data\\case.xlsx'

list_id, list_name, list_method, list_url, list_key,list_params, list_anticipate = dataParsing(filepath)
# print(list_id, listname, list_method, list_url, list_key,list_params, list_anticipate)

@logger("用例测试")
def caseInterface():
    list_pass = 0   #成功用例数量
    list_fail = 0   #失败用例数量
    list_return_json = []  #返回json列表
    list_result_status = []    #返回状态
    list_unknown = 0    #未知错误数量
    list_abnormal = 0    #异常用例（abnormal：异常）
    error_num = 0
    for listurl,listparams,listmethod,listanticipate in zip(list_url,list_params,list_method,list_anticipate):
        while error_num <= Config_Try_Num:
            method = str(listmethod)    #将请求方法转换为字符串，必须
            params = json.loads(listparams) #将请求参数转换为json格式，必须
            # 打印接口请求所有参数格式，url为字符串，参数为字典json格式，方法为字符串
            # print((type(TestPlanUrl + listurl)), type(params), type(method))
            #调用InterfaceBase.base.py文件中的RequestApi类，开始测试
            api = RequestApi(url = TestPlanUrl+listurl,params = params, method=method )
            api_json=api.getJson()  #获取接口返回的json数据
            assert_re = assert_in(anticipate=listanticipate, return_json=api_json)
            print(assert_re)
            if api_json['code'] == 0:
                LOG.info('case:code=0> 参数:%s, url:%s ,返回:%s,预期:%s' % (list_params, list_url, api_json, list_anticipate))
                # print("预期",list_anticipate)
                assert_re = assert_in(anticipate=listanticipate,return_json=api_json)
                if assert_re['code'] == 0:
                    list_return_json.append(api_json['return_result_json'])
                    list_result_status.append('pass')
                    list_pass += 1
                    error_num = 0
                    break
                elif assert_re['code'] == 1:
                    if error_num <= Config_Try_Num:
                        error_num += 1
                        LOG.info("code=1 失败重试中")
                    else:
                        LOG.info("code=1 失败重试次数用完，最后结果")
                        error_num = 0
                        list_fail += 1
                        list_result_status.append('fail')
                        list_return_json.append(api_json['return_result_json'])
                        break
                elif assert_re['code'] == 2:
                    if error_num < Config_Try_Num:
                        error_num += 1
                        LOG.info('code=2 失败重试中')
                    else:
                        LOG.info("code=2 失败重试次数用完，最后结果")
                        error_num = 0
                        list_abnormal += 1
                        list_result_status.append(assert_re['return_result_json'])
                        break
                else:
                    if error_num < Config_Try_Num:
                        error_num += 1
                        LOG.info('无code，失败重试中')
                    else:
                        LOG.info('无code,失败重试次数用完，最后结果')
                        error_num = 0
                        list_unknown += 1
                        list_result_status.append('无code,未知错误')
                        list_return_json.append('无code,未知错误')
                        break
            else:
                if error_num <Config_Try_Num:
                    error_num += 1
                    LOG.info('最终失败重试中')
                else:
                    LOG.info('最终失败,失败重试中次数用完，最后结果')
                    error_num = 0
                    list_abnormal += 1
                    list_result_status.append('exception')
                    list_return_json.append(api_json['result'])
                    break
    return list_result_status,list_fail,list_pass,list_return_json,list_abnormal,list_unknown

if __name__ == "__main__":
    A = caseInterface()
    print(A)
