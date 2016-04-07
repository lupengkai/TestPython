f = open('/home/tage/Documents/12.txt', 'r')
print(f.read())

try:
    f = open('/home/tage/Documents/12.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/home/tage/TestHTTP.java', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open("../thunb.jpg", 'rb') as f:
    print(f.read())

with open('char.txt', 'r', encoding='gbk') as f:
    print(f.read())

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())

f = StringIO('Hello \t 999 \n Hi \n Goodbye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO

f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

print(f.read())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())
print(f.getvalue())

import os

print(os.name)
print(os.uname())
print(os.environ)

print(os.environ.get('PATH'))

print(os.environ.get('PATH', 'default'))

print(os.path.abspath('.'))

# os.path.join('/home/tage', 'testpythonos')
# os.mkdir('/home/tage/testpythonos')
# os.rmdir('/home/tage/testpythonos')

print(os.listdir('.'))
