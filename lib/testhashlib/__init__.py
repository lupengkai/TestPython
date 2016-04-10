import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md5_1 = hashlib.md5()
md5_1.update('how to use md5 '.encode('utf-8'))
md5_1.update('in python hashlib?'.encode('utf-8'))
print(md5_1.hexdigest())
# 32位的16进制字符串

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
# 40位的16进制字符串表示

# 网站登陆
