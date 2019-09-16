# coding:utf-8
#heboqiang
#

#
# import  json
# from utils.public import *
# from utils.operationJson import  OperationJson
# from utils.operationExcel import  OperationExcel
#
# operationJson=OperationJson()
# operationExcel=OperationExcel()
#
# def setSo(kd='自动化测试工程师'):
# 	'''对搜索的数据重新赋值'''
# 	dici1=json.loads(operationJson.getRequestsData(1))
# 	dici1['kd']=kd
# 	return dici1
#
# def writePositionId(content):
# 	'''把职位的ID写到文件中'''
# 	with open(data_dir(fileName='positionId'),'w') as f:
# 		f.write(content)
#
# def getPositionId():
# 	'''获取职位招聘的信息'''
# 	with open(data_dir(fileName='positionId'),'r') as f:
# 		return json.loads(f.read())
#
# def getUrl():
# 	listUrl=[]
# 	for item in getPositionId():
# 		url='https://www.lagou.com/jobs/{0}.html'.format(item)
# 		listUrl.append(url)
# 	return listUrl
#
#
#
#
#
