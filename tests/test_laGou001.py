# # coding:utf-8
# #heboqiang
#
#
# import  unittest
# import  json
# from base.method import Method,IsContent
# from page.laGou import *
# from page.diyi1 import *
# from utils.public import *
# from utils.operationExcel import OperationExcel
# from utils.operationJson import OperationJson
# from common.logger import Log
#
# from common.db import *  # 导入db.py文件，源码见上篇
#
# # 数据准备
# NOT_EXIST_USER = '范冰冰'
# EXIST_USER = '张三'
#
# class LaGou(unittest.TestCase):
# 	log = Log()
# 	def setUp(self):
# 		self.obj=Method()
# 		self.p=IsContent()
# 		self.execl=OperationExcel()
# 		self.operationJson=OperationJson()
#
# 	def statusCode(self,r):
# 		self.assertEqual(r.status_code, 200)
# 		self.assertEqual(r.json()['result_code'], 200)
#
# 	def isContent(self,r,row):
# 		self.statusCode(r=r)
# 		self.assertTrue(self.p.isContent(row=row,str2=r.text))
#
# 	def test_laGou_001(self):
# 		# # 环境检查
# 		# if check_user (NOT_EXIST_USER):
# 		# 	del_user (NOT_EXIST_USER)
# 		'''测试1'''
# 		self.log.info ("------登录失败用例：start!---------")
# 		r = self.obj.post(row=1,data=self.operationJson.getRequestsData(1))
# 		print(type(self.operationJson.getRequestsData(1)))
# 		print ("test_laGou_001 is:", r.text)
# 		print(type(self.operationJson.getRequestsData(1)))
# 		self.log.info("获取请求结果：%s"%r.text)
# 		self.isContent(r=r,row=1)
# 		# 数据库断言
# 		# self.assertTrue (check_user (NOT_EXIST_USER))
# 		self.execl.writeResult(1,'pass')
# 		# 环境清理
# 		# del_user (NOT_EXIST_USER)
#
#
# 	# def test_laGou_003(self):
# 	# 	"sign为空"
# 	# 	r = self.obj.post(row=2,data=set_so_keyword(app_id='201808291707251386531'))
# 	# 	print ("test_laGou_002 is:", r.text)
# 	# 	self.isContent (r=r, row=2)
# 	# 	self.execl.writeResult (2,'pass')
#
#
#
#
