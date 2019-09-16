#!/use/bin/env python
#coding:utf-8


import  unittest
import  os
import  smtplib
from email.mime.text import MIMEText
import time
import HTMLTestRunner
from common.logger import Log

from utils.operationExcel import OperationExcel

from configs.readCofig import *


class Runner:
	def __init__(self):
		self.excel=OperationExcel()
		self.log = Log()

	def getSuite(self):
		'''获取要执行的测试套件'''
		suite = unittest.TestLoader().discover(
			start_dir=os.path.join((os.path.dirname(__file__)), 'tests'),
			pattern='test_*.py',
			top_level_dir=None)
		return suite

	# def send_mail(self,to_user,sub,content):
	# 	'''
	# 	发送邮件内容
	# 	:param to_user:发送邮件的人
	# 	:param sub:主题
	# 	:param content:邮件内容
	# 	'''
	# 	global  send_mail
	# 	global  send_user
	# 	send_mail = send_mail_1
	# 	send_user= send_user_1
	# 	message=MIMEText(content,_subtype='plain',_charset='utf-8')#创建一个实例，这里设置为html格式邮件
	# 	message['Subject']=sub#设置主题
	# 	message['From']=send_user
	# 	message['To']=to_user
	# 	server=smtplib.SMTP()
	# 	server.connect(send_mail)#连接smtp服务器
	# 	server.login('hbqfighting@163.com' ,'hbq19941120')#登陆服务器
	# 	server.sendmail(send_user,to_user,message.as_string())#发送邮件
	# 	server.close()

	def run_case(self,getSuite, reportName="report"):
		# 当前脚本所在文件真实路径
		cur_path = os.path.dirname (os.path.realpath (__file__))
		print (cur_path)
		'''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
		now = time.strftime ("%Y_%m_%d_%H_%M_%S")
		report_path = os.path.join (cur_path, reportName)  # 用例文件夹
		# 如果不存在这个report文件夹，就自动创建一个
		if not os.path.exists (report_path): os.mkdir (report_path)
		report_abspath = os.path.join (report_path, now + "result.html")
		print ("report path:%s" % report_abspath)
		fp = open (report_abspath, "wb")
		runner = HTMLTestRunner.HTMLTestRunner (stream=fp,
												title='自动化测试报告,测试结果如下：',
												description='用例执行情况：')

		# 调用getSuite函数返回值
		runner.run (getSuite)
		fp.close ()

	def get_report_file(self):
		# # 当前脚本所在文件真实路径
		# cur_path = os.path.dirname (os.path.realpath (__file__))
		report_path = os.path.join((os.path.dirname(__file__)), 'report')  # 用例文件夹
		'''第三步：获取最新的测试报告'''
		lists = os.listdir (report_path)
		lists.sort (key=lambda fn: os.path.getmtime (os.path.join (report_path, fn)))
		print (u'最新测试生成的报告： ' + lists[-1])
		# 找到最新生成的报告文件
		report_file = os.path.join (report_path, lists[-1])
		return report_file

	def main_run(self):
		self.log.info ("================================== 测试开始 ==================================")
		'''批量执行测试用例'''
		unittest.TextTestRunner().run(self.getSuite())
		content='通过数：{0} 失败数：{1} 通过率：{2}'.format(
			self.excel.run_success_result(),
			self.excel.run_fail_result(),self.excel.run_pass_rate())
		print('Please wait while the statistics test results are sent in the mail')
		# self.send_mail(to_user_1,'接口自动化测试报告',content)
		self.run_case(self.getSuite())  # 2执行用例
		self.get_report_file()
		self.log.info ("================================== 测试结束 ==================================")

if __name__ == '__main__':
	Runner().main_run()
