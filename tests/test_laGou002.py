# # coding:utf-8
# #heboqiang
#
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
#
# class LaGou(unittest.TestCase):
# 	def setUp(self):
# 		self.obj=Method()
# 		self.p=IsContent()
# 		self.execl=OperationExcel()
# 		self.operationJson=OperationJson()
#
# 	# def statusCode(self,r):
# 	# 	# self.assertEqual(r.status_code, 200)
# 	# 	self.assertEqual(r.json()['result_code'], 401)
#
# 	def isContent(self,r,row):
# 		# self.statusCode(r=r)
# 		self.assertTrue(self.p.isContent(row=row,str2=r.text))
#
# 	def test_laGou_001(self):
# 		'''测试1'''
# 		# r = self.obj.post(row=1,data=self.operationJson.getRequestsData(1))
# 		r = self.obj.post (row=1, data=set_so_keyword (app_id='20180829170725138653', sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))
# 		print ("test_laGou_001 is:", r.text)
# 		self.assertEqual(r.json()['result_code'], 200)
# 		self.isContent(r=r,row=1)
# 		self.execl.writeResult(1,'pass')
#
# 	def test_laGou_002(self):
# 		'''错误测试'''
# 		r = self.obj.post(row=2,data=self.operationJson.getRequestsData(2))
# 		self.assertEqual(r.json()['result_code'], 403)
# 		print ("test_laGou_001 is:", r.text)
# 		self.isContent (r=r, row=2)
# 		self.execl.writeResult (2, 'pass')
#
# 	def test_laGou_004(self):
# 		"sign为空"
# 		r = self.obj.post(row=3,data=set_so_keyword(app_id=201808291707251386534444))
# 		print ("test_laGou_002 is:", r.text)
# 		self.assertEqual(r.json()['result_code'], 403)
# 		self.isContent (r=r, row=3)
# 		self.execl.writeResult (3,'pass')