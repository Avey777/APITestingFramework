# -*- coding: utf-8 -*-
"""
字典读取处理数据
"""
'''字典取值'''

def res(dt,code):
    result=[]
    if isinstance(dt, dict) and code in dt.keys():
        value = dt[code]
        result.append(value)
        return result
    elif isinstance(dt, (list, tuple)):
            for item in dt:
                value=res(item,code)
                if value =="None" or value is None:
                    pass
                elif len(value)==0:
                    pass
                else:
                    result.append(value)
            return result
    else:
        if isinstance(dt, dict):
            for k in dt:
                value=res(dt[k], code)
                if value =="None" or value is None :
                    pass
                elif len(value)==0:
                    pass
                else:
                    for item in value:
                        result.append(item)
            return result

if __name__ == "__main__":
    # res('IsPass',{'code': 0, 'result_json': {'Message': '登录成功!', 'IsPass': True}})
    # res("d",2)
    pass