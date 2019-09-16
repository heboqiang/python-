# coding:utf-8
#heboqiang



import  unittest
import  json
from base.method import Method,IsContent
from page.laGou import *
from page.diyi1 import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class LaGou(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.p=IsContent()
		self.execl=OperationExcel()
		self.operationJson=OperationJson()

	def statusCode(self,r):
		# self.assertEqual(r.status_code, 200)
		print(r.json()['code'])
		self.assertEqual(r.json ()['code'], '1001')

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.p.isContent(row=row,str2=r.text))

	def test_laGou_001(self):
		"sign为空"
		r = self.obj.post(row=1,data=set_so_keyword(userPhone="18821768014"))
		print ("test_laGou_004 is:", r.text)
		self.isContent (r=r, row=1)
		self.execl.writeResult (1,'pass')
# print (set_so_keyword(app_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))p_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))