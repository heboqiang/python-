
from common.DES_CBC import *
import base64
import binascii

text = "18821768014"
print(text)
# print("Plaintext : "+text)
KEY = "1f4f8a113b4a5d66"
IV = [0]*40 + [1]*20 + [0]*4
# print(type(IV))
# print("***********初始配置信息*************")
# print("KEY : " + KEY)
#IV_str = "".join(IV)
# print("IV : " ,IV)
# print("************************************")

# cypher_text = CBC_DES_ENC(IV,text,KEY)
# c = "".join(cypher_text)
# e = 0  #暂存结果
# for i in c:
#   d = ord(i) #单个字符转换成ASCii码
#   e = e*256 + d  #将单个字符转换成的ASCii码相连
# # print("e:%x" %e)
# print(type(e))
# print("Encryption:%x" %e)

original_text = CBC_DES_DEC(IV,CBC_DES_ENC(IV,text,KEY),KEY)
b = "".join(original_text)
print(type(b))
print("Decryption : "+ b)