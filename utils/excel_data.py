#!/use/bin/env python
#coding:utf-8


class ExcelVariable:
	caseID=0
	url=4
	request_data=5
	expect=6
	result=7

def getCaseID():
	return ExcelVariable.caseID

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def get_request_data2():
	return ExcelVariable.request_data

def getExpect():
	return ExcelVariable.expect

def getResult():
	return ExcelVariable.result

def getHeadersValue():
	'''获取请求头'''
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
		'Cookie':'_ga=GA1.2.379553215.1541825947; user_trace_token=20181110130019-85c41866-e4a5-11e8-95d7-525400f775ce; LGUID=20181110130019-85c41cee-e4a5-11e8-95d7-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166fbfd1f531f3-07a19d38569bf3-5e442e19-1049088-166fbfd1f552d0%22%2C%22%24device_id%22%3A%22166fbfd1f531f3-07a19d38569bf3-5e442e19-1049088-166fbfd1f552d0%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; index_location_city=%E6%9D%AD%E5%B7%9E; LG_LOGIN_USER_ID=d2c7bee1ca6d40aef3277fbc5c7eac8889629f3c205acd9f503744515abb887a; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; JSESSIONID=ABAAABAAAIAACBI7F74E1042637C48634E39665FA066D17; _gid=GA1.2.1143021156.1548073985; _putrc=467C9CB7D9A917CD123F89F2B170EADC; login=true; unick=%E4%BD%95%E5%8D%9C%E5%BC%BA; TG-TRACK-CODE=index_search; WEBTJ-ID=20190122151917-168746d785d78-007c47a7b3c0d4-6313363-1049088-168746d785f3a; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546175256,1547475905,1548073985,1548141559; LGSID=20190122152228-79654a11-1e16-11e9-b735-5254005c3644; SEARCH_ID=113a4fd6140844f8b01d723f8c122383; gate_login_token=6b5250a90bd4521c627c623e00d9e1136455951a9f8d46011058013b71fe9095; _gat=1; LGRID=20190122160506-6e1d85c3-1e1c-11e9-b735-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1548144119',
		'Referer':'https://www.lagou.com/jobs/list_Python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E6%9D%AD%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput='}
	return headers
