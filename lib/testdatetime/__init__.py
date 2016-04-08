from datetime import datetime

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2016, 4, 8, 10, 14)
print(dt)

print(dt.timestamp())

t = dt.timestamp()
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now.strftime('%a, %b, %d %H:%M'))

from datetime import timedelta

print(now + timedelta(hours=10))
print(now + timedelta(days=1, hours=10))
