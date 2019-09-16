#!/use/bin/env python
#coding:utf-8 

import  os

def data_dir(data='data',fileName=None):
	'''查找文件的路径'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)

