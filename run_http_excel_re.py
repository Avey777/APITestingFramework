#!/usr/bin/env python
# coding: utf-8
# from Public.email_send import send_mali_byQQ, send_mali_by163
from Case.case import caseInterface
from Public.pyreport_excel import create
import os, datetime
from Public.get_excel import dataParsing


def start_excel_report_http():
    m = datetime.datetime.now().strftime("%Y-%m%d-%H%M")
    basdir = os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '\\data\\case.xlsx'
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = dataParsing(path)
    listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi = caseInterface()
    filepath = os.path.join(basdir + '\\Report\\%s-result.xls' % m)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    create(filename=filepath, list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey, listconeents=listconeent, listfangshis=listfangshi, listqiwangs=listqiwang,
           listids=listid, listrelust=listrelust, listnames=listname)
    # contec = 'dubbo接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    #     list_pass, list_fail, list_exption, list_weizhi, filepath)
    # send_mali_byQQ("123456@qq.com", "yvghvyhqcbdbb","1234564@qq.com","123", filepath)


if __name__ == '__main__':
    start_excel_report_http()
