import itertools

natuals = itertools.count(1)
# for n in natuals:
#     print(n)

cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)


ns = itertools.repeat('A', 3)  # 第2个参数不写，不限次数
for n in ns:
    print(n)

ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

l1 = list([1, 2, 4])
l2 = list((1, 2, 4))
l3 = list('3425')

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('dafdaaaa111'):
    print(key, list(group))

print(group)

print(ns)

for key, group in itertools.groupby('dDdaAAfdaAAaa111', lambda c: c.upper()):
    print(key, list(group))
