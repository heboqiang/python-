# coding:utf-8
#heboqiang

import  json
from utils.public import *
from utils.operationJson import  OperationJson
from utils.operationExcel import  OperationExcel

operationJson=OperationJson()
operationExcel=OperationExcel()

def set_so_keyword(userPhone=None):
    "获取请求参数"
    data = json.loads(operationJson.getRequestsData(1))
    data["userPhone"] = userPhone
    return json.dumps(data)
print(type(set_so_keyword()))


# def set_so_keyword(app_id=None,sign=None):
#     "获取请求参数"
#     data = json.loads(operationJson.getRequestsData(1))
#     data["app_id"] = app_id
#     data["sign"] = sign
#     return json.dumps(data)
# print(type(set_so_keyword()))

# print(set_so_keyword(app_id=20180829170725138653488,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))