from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

print(isinstance(p, tuple))

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key2'])

from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] += 1
