# \d
# \w
# \s
# .
# * + ? {n} {n,m}

# [0-9a-zA-Z\_]
# [a-zA-Z\_][0-9a-zA-Z\-]*
# [P|p]
# ^ ^\d
# $ \d$

# s = 'ABC\\-001'
# s = r'ABC\-001'

import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

test = 'abc'

if re.match(r'cbd', test):
    print('ok')
else:
    print('failed')

print(re.split(r'\s+', 'a b       c'))

print(re.split(r'[\s\,\;]+', 'a,b;c  d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(re.match(r'^(\d+)(0*)$', '102300').groups())

re_telphone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telphone.match('010-12345').groups())
