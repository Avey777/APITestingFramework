#!/usr/bin/env python
# coding: utf-8
"""
读取excel文件，单独文件
不基于任何文件，只需要读取的excel文件路径正确，格式正确
格式 -- 第一列：用例编号id；第二列：用例标题；第三列：用例请求方法
    第四列：用例key值；第五列：请求不完全url；第六列：请求json参数
    第七列：期望值
"""
import os

import xlrd
from Public.log import logger, LOG


@logger('解析测试用例文件')
def dataParsing(filrpath):
    try:
        file = xlrd.open_workbook(filrpath) #打开xlsx工作簿
        file.encoding = 'utf8'  #工作簿编码转换为utf8
        me = file.sheets()[0]   #读取工作簿中的第一个表格
        nrows = me.nrows    #

        list_id = []     #用例编号id
        list_name = []  # 用例名称
        list_method = []  # 请求方式，POST、GET
        list_url = []  # 测试url
        list_key = []  #请求key值，暂不使用
        list_params = [] #请求参数
        list_anticipate = []    #预期
        listrelut = []    #结果，暂不使用

        for i in range(1, nrows):
            list_id.append(me.cell(i, 0).value)  #“用例编号”追加到列表，读取excel第一列
            list_name.append(me.cell(i, 1).value) #“用例标题”追加到列表，读取excel第二列
            list_method.append((me.cell(i, 2).value))  # “用例请求方法”追加到列表，读取第三列
            list_url.append(me.cell(i, 3).value)  # “用例请求url（自定义部分）追加到列表”，读取第四列
            list_key.append(me.cell(i, 4).value)  # “用例key值”追加到列表，读取excel第五列
            list_params.append(me.cell(i, 5).value) #“用例请求参数”追加到列表，读取excel第六列
            list_anticipate.append((me.cell(i, 6).value))   #“用例预期结果”追加到列表，读取第七列
        #返回读取列表
        return list_id, list_name, list_method, list_url, list_key,list_params, list_anticipate
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s' % e)


@logger('生成数据驱动所用数据')
def makedata():
    import os
    # path = os.getcwd() + '\\data\\case.xlsx'  #运行最外层页面启用
    path = os.path.dirname(os.getcwd()) + '\\data\\case.xlsx'   #运营本页面时启用
    # print(path)
    listid, listname, listmethod,listurl, listkey ,  listparams, listanticipate = dataParsing(path)
    # print(listid, listname, listmethod, listparams, listurl,  listanticpate)
    make_data = []
    for i in range(len(listid)):
        make_data.append({'method': listmethod[i],'url': listurl[i],'key': listkey[i], 'params': listparams[i],
                          'anticipate': listanticipate[i]})
        i += 1
    return make_data


if __name__ == "__main__":
    path = os.path.dirname(os.getcwd()) + '\\data\\case.xlsx'
    print(dataParsing(path))
    print("---------"*5)
    print(makedata())
