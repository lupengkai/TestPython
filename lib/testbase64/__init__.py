import base64

s = base64.b64encode(b'binary\x00string')
print(s)

b = base64.b64decode(s)
print(b)

s1 = base64.urlsafe_b64decode(b'abcd--__')
print(s1)

s2 = base64.urlsafe_b64decode(b'abcd++//')
print(s2)
