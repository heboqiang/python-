# coding:utf-8
#heboqiang

import os
import configparser

cur_path = os.path.dirname(os.path.relpath(__file__))
configpath  = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configpath,encoding="utf-8")

send_mail_1 = conf.get('email','send_mail')

send_user_1 = conf.get('email','send_user')

# login_1 = conf.get('email','login')

to_user_1 = conf.get('email','to_user')

send_mail_ren_1 = conf.get('email','send_mail_ren')


