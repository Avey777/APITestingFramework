# -*- coding: utf-8 -*-
# @Author
import os,datetime,time

from Case.case import caseInterface
from Dingtalk.Dingtalk import send_ding
from Public.py_Html import createHtml
from Public.get_excel import dataParsing
from WechatTalk.wechat_msgs import wechatSendmessages

'''执行测试的主要文件'''
def start_interface_html_http():
    starttime=datetime.datetime.now()
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir=os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '\\data\\case.xlsx'
    print(path)
    listid, listname, listmethod, listurl, listkey, listparams, listanticipate = dataParsing(path)
    listrelust, list_fail, list_pass, list_json,list_abnormal,list_unknown = caseInterface()
    filepath =os.path.join(basdir+'\\Report\\%s-result.html'%day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime=datetime.datetime.now()
    createHtml(titles=u'http接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listparams,url=listurl,meth=listmethod,
               yuqi=listanticipate,json=list_json,relusts=listrelust,weizhi=list_unknown,exceptions=list_abnormal)
    contec_messages = u'http接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    list_pass, list_fail, list_abnormal, list_unknown, filepath)
    try:
        send_ding(content=contec_messages)
    except:
        print("钉钉发送消息失败")
    try:
        open(filepath)
        wechatSendmessages(msg=contec_messages+filepath)
    except:
        print("企业微信消息发送失败")

if __name__ == '__main__':
    start_interface_html_http()