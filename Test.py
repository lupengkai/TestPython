__author__ = 'tage'


def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


def nop():
    pass


import math

math.sqrt(2)


def quadratic(a, b, c):
    r1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    r2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return r1, r2


r = quadratic(1, -2, 1)

print(r)


def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1

    return s


print(power(2))
print(power(2, 3))


def enroll(name, gender, age=6, city='Beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)


enroll('make', 2)
enroll('haha', 'e', 9)
enroll('keke', 'g', city='Tianjin')


def add_end(L=[]):
    L.append('end')
    return L


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())


# print(L)

def add_end_1(L=None):
    L = []
    L.append("end")
    return L


print(add_end_1())
print(add_end_1())


def calc(numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum


print(calc([1, 2, 3]))  # list
print(calc((1, 2, 3)))  # tuple fixed


def calc(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum


print(calc(1, 2, 4))
num = [1, 2, 4]
print(calc(*num))
num = (1, 2, 3)
print(calc(*num))
print(calc())


def calc(*numbers):
    sum = 0
    for num in numbers:
        num = num - 1
        print(num)
    print(numbers)
    return numbers


print(calc(*num))


def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)


person('Ben', 20, city='Beijing', tel='A10')
extra = {'sex': 'naha', 'job': 'male'}
person('Nick', 19, **extra)
extra['haah'] = 123
print(extra)


def person(name, city, *, age, job='IT'):
    pass


person('Bob', 'Beijing', age=18, job='IT')
person('Bob', 'Beijing', age=18)


def people(name):
    print(name)


people(**{'name': 'Lily'})


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(100))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)
        return


move(3, 'A', 'B', 'C')

L = [1, 2, 3, 4]
r = []
for i in range(3):
    r.append(L[i])
print(r)

r = L[:3]
print(r)
print(L[1:4])

print(L[-1])
print(L[-0])
print(L[2:-1])
print(L[:])
print(L[3:])
print(L[::2])
print(L[::2])

T = (1, 2, 3, 4, 5)
print(T[1:2])

H = (5,)
print(H)
S = 'abcdefg'
print(S[0:4:1])

D = {'Lily': 'Dream', 'Daniel': 'Work', 'Ben': 'Study'}
for p in D:
    print(p)

for p in D.values():
    print(p)

for p in D.items():
    print(p)

for p in enumerate(D):
    print(p)
for x, y in enumerate(D):
    print(x)
    print(y)
list((1, 2))
list('1234')
L = list({'1': 2, '2': 3})
print(L)
print([x * x for x in range(1, 10)])
print([x * x for x in range(1, 10) if x % 2 == 0])

print([m + n for m in 'abx' for n in 'xyz'])

import os

print([d for d in os.listdir('/')])

L = ['Hello', 'World', 'Apple']
print([s.lower() for s in L])
L1 = ['Hello', 'World', 'Apple', 18]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
r = (x for x in range(1, 10))
print(next(r))
for x in r:
    print(x)
for x in r:
    print(x)


def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        print(b)
        a, b = b, a + b
        i = i + 1
    return 'done'


fib(6)


def fib(n):
    i, a, b = 0, 0, 1
    while i < n:
        yield b
        a, b = b, a + b
        i = i + 1
    return 'done'


print(next(fib(6)))


def triangles():
    L = [1]
    while 1:
        yield L
        L1 = L + [0]
        L2 = [0] + L
        L = [L1[i] + L2[i] for i in range(0, len(L1))]


n = 1
for i in triangles():
    print(i)
    n = n + 1
    if n == 10:
        break

from collections import Iterable
from collections import Iterator

print(isinstance(triangles(), Iterator))
print(isinstance(triangles(), Iterable))
print(isinstance((x for x in range(1, 10)), Iterable))
print(isinstance(range(10), Iterable))
print(isinstance(iter('abc'), Iterable))


def add(x, *fs):
    S = [f(x) for f in fs]
    print(S)


add(2, abs, abs)


def power(x):
    return x * x


print(list(map(power, [1, 2, 3, 4, 5])))


def plus(a, b):
    return a + b


from functools import reduce

print(reduce(plus, [x for x in range(10)]))


def char2num(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]


def fn(x, y):
    return 10 * x + y


print(reduce(fn, map(char2num, '12345')))


def str2int(s):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    def fn(x, y):
        return 10 * x + y

    return reduce(fn, map(char2num, s))


print(str2int('12345'))


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('23567'))


def normalize(name):
    s = name[0].upper()
    for c in name:
        s = s + c.lower()
    return s


print(normalize('hhKK'))

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def normalize(name):
    return name[0].upper() + name[1:].lower()


print(normalize('hhjsKKS'))


def prod(L):
    return reduce(lambda x, y: x * y, L)


print(prod([x for x in range(1, 5)]))


def str2float(s):
    s1=''
    for c in s:
        if c != '.':
            s1 = s1+c
    return reduce(lambda x, y: 10 * x + y, map(char2num, s1)) / (10 ** (len(s) - s.index('.') - 1))


print(str2float('12.35'))


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 3, 3, 4])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, [' 1', '2', '', ' ', None])))


def _odd_iter():  # 奇数惰性序列
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):  # 过滤函数
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 20:
        print(n)
    else:
        break


# ! list(123)



def is_palindrome(n):  # 过滤函数
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, range(1, 10))))

print(sorted([1, 2, 3, 4, -6]))
print(sorted([1, 2, 3, 4, -6], key=abs))
print(sorted([1, 2, 3, 4, -6], key=abs, reverse=True))

print(sorted(['azz', 'sss', 'As', 'Zdd'], key=str.upper))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)
