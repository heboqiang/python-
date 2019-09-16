# # coding:utf-8
# #heboqiang
#
#
# import  unittest
# import  json
# from urllib.parse import urlencode
#
# from base.method import Method,IsContent
# from page.laGou import *
# from page.diyi1 import *
# from utils.public import *
# from utils.operationExcel import OperationExcel
# from utils.operationJson import OperationJson
# import urllib.request
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
# 	# 	# self.assertEqual (r.json ()['result_code'], 1006)
#
# 	# def isContent(self,r,row):
# 		# self.statusCode(r=r)
# 		# self.assertTrue(self.p.isContent(row=row,str2=r.text))
#
# 	# def test_laGou_004(self):
# 	# 	"sign为空"
# 	# 	r = self.obj.post(row=3,data=set_so_keyword(app_id="20180829170725138653"))
# 	# 	print ("test_laGou_004 is:", r.text)
# 	# 	self.isContent (r=r, row=3)
# 	# 	self.execl.writeResult (3,'pass')
# 	#
# 	def test_laGou_001(self):
# 		'''测试1'''
# 		r = self.obj.dubbo(row=5,param=self.operationJson.getRequestsData(5),method='tradeDetailQuery')
# 		# print(type(json.loads(self.operationJson.getRequestsData(5))))
# 		print (self.operationJson.getRequestsData(5))
# 		print(r.text)
# 		# print ("test_laGou_001 is:", r.text)
# 		# print(r.url)
# 		#
# 		# pp = urlencode(urllib.request.unquote(r.url))
# 		# print(pp)
# 		# print(urllib.request.unquote(r.url))
# 		# print(urlencode(pp))
# 		# print (r.url)
# 		# print(urllib.request.unquote(self.operationJson.getRequestsData(4)))
# 		# print(self.operationJson.getRequestsData(4))
# 		# print(urlencode(self.operationJson.getRequestsData(4)))
#
# 		# print(self.operationJson.getRequestsData(4))
# 		# print((self.execl.getUrl(4)+self.operationJson.getRequestsData(4)))
# 		# self.isContent(r=r,row=5)
# 		# self.execl.writeResult(5,'pass')
#
# # 	def test_laGou_004(self):
# # 		r = self.obj.get(url='https://www.cnblogs.com/mvc/Blog/CommentForm.aspx?postId=3845123&blogApp=siyunianhua&_=1557553713217,timeout=6')
# # # print (set_so_keyword(app_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))