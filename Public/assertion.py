# -*- coding: utf-8 -*-
"""
encapsulation_dict:封装技术
anticipate 预期—数据
return 返回—数据
使用是需要预期格式：IsPass=True
"""
from Public.log import logger, LOG

"""断言方法封装"""
from Public.encapsulation_dict import res

@logger('断言')
def assert_in(anticipate,return_json):
    if len(anticipate.split('=')) > 1:
        #预期数据处理
        anticipate_data = anticipate.split('&')    #预期结果处理
        print("预期数据",anticipate_data)  #打印预期处理梳理
        anticipate_dict = dict([(item.split('=')) for item in anticipate_data]) #将预期值转换为字典格式
        print("预期格式转换为字典格式数据",anticipate_dict)
        #取值字典
        anticipate_value = "".join([(str(value)) for value in anticipate_dict.values()])
        print("预期值",(anticipate_value))

        # 返回数据处理
        # return_value = "".join([(str(res(return_json, key))) for key in anticipate_dict.keys()])
        # print("返回值",return_value)

        print(return_json)
        #暂时使用此断言，字典获取value值格式需要优化
        if anticipate_value in str(return_json):
        # if anticipate_value in return_value:  #未处理好，赞不使用
            LOG.info("断言成功")
            return  { 'code':0,"result":'pass'}
        else:
            LOG.info('断言失败')
            return {'code':1,'result':'fail'}
    else:
        LOG.info('断言错误，请填写测试预期值')
        return  {"code":2,'result':'断言错误，请检查预期值'}


@logger('断言测试结果')
def assertre(anticipate):
    if len(anticipate.split('=')) > 1:
        data = anticipate.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('断言，填写测试预期值')
        raise {"code":1,'result':'断言，填写测试预期值'}

if __name__ == '__main__':
    a = assert_in('IsPass=True',{'code': 0, 'result_json': {'Message': '登录成功!', 'IsPass': True}})

    print(a)