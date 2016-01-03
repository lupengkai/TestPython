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
    s1 = ''
    for c in s:
        if c != '.':
            s1 = s1 + c
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


def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s = s + n
        return s

    return sum


f = lazy_sum(1, 2, 3)

print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

f = lambda x: x * x
print(f(5))


def build(x, y):
    return lambda: x + y


f = build(1, 2)

print(f())

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2016-1-1')


print(now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2016-1-1')


print(now.__name__)


def log(func):
    def wrapper(*args, **kw):
        return func(*args, **kw)

    print('begin call %s():' % func.__name__)
    return wrapper


@log
def now():
    print('2016-1-1')


now()

print(int('110'))
print(int('110', base=2))


def int2(s):
    return int(s, base=2)


import functools

int2 = functools.partial(int, base=2)

print(int2('110'))


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart', 59)
lisa = Student('Lisa', 99)
lisa.print_score()
bart.print_score()


class Student(object):
    pass


nike = Student()
nike.name = 'Nike'
print(nike.name)

lucy = Student


# lucy.name

class Person(object):
    def __init__(self, name):
        self.__name = name

    def print_name(self):
        print('name: %s' % self.__name)


peter = Person('peter')
peter.print_name()


# print(peter.__name)
# print(peter._Student__name)//不同的python解释器会把__name解释成不同变量名

class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


def see_run(animal):
    animal.run()


class Apple(object):
    def run(self):
        print('apple can\'t run')


see_run(Dog())
see_run(Cat())
see_run(Animal())
see_run(Apple())

apple = Apple()
print(isinstance(Cat(), Animal))
print(isinstance(Animal(), Cat))

print(type(123))
print(type(Student))
print(type(apple))
print(type(None))
print(type(int))
print(type(''))
print(type(str))
print(type(abs))

import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(1, 10))) == types.GeneratorType)

print(isinstance((1,), tuple))
print(isinstance((1,), (tuple, list)))
apple.name = 'apple'

print(dir(apple))
print(dir(Apple))

print(len('ABc'))
print('Abc'.__len__())

print(hasattr(apple, 'run'))

f = getattr(apple, 'run', 404)
print(f())


class Car(object):
    def __init__(self, name, size):
        self.__name = name
        self.size = size


c = Car('BMW', '5')
print(hasattr(Car, '__name'))
print(hasattr(Car, 'size'))
print(hasattr(c, '__name'))
print(hasattr(c, 'size'))
print(dir(Car))
print(dir(c))
print(dir(type))
print(type(type))


# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None


class Teacher(object):
    name = 'teacher'


t = Teacher()
print(Teacher.name)
print(t.name)
Teacher.age = 10
print(t.age)
print(Teacher.age)
t1 = Teacher()
Teacher.name = 'TT'
print(t1.name)
Teacher.name = 'BB'
print(t1.name)
print(t.name)
t.name = 'tt'
print(t.name)
print(t1.name)
# del Teacher.name
print(t.name)
# print(t1.name)
del t.name
print(t.name)


class School(object):
    pass


def set_size(self, size):
    self.size = size


from types import MethodType

s = School

s.set_size = MethodType(set_size, s)

s.set_size(20)
print(s.size)
print(dir(s))
School.set_size = MethodType(set_size, School)
School.set_size(100)
print(dir(School))

s1 = School()
s1.set_size(200)

print(s1.size)  # 类的变量方法，实例没有自己的一份
print(School.size)
print(dir(s1))


class Student(object):
    __slots__ = ('name', 'age')


Student.name = 'XD'
Student.age = '83'

Student.size = 300

s1 = Student()
print(s1.size)


# s1.size = 200

# s1.id = '1212'

# s1.name = 'haha'#AttributeError: 'Student' object attribute 'name' is read-only

class Book(object):
    pass


b = Book()
b.name = 'b'
Book.name = 'book'
print(b.name)
print(Book.name)


class Pen(object):
    pass


Pen.name = 'pen'
p = Pen()
p.name = 'p'  # p.name独立出来

print(Pen.name)
print(p.name)


class Computer(object):
    __slots__ = ('name', 'age')


c = Computer()
print(dir(c))
c.name = 'c'
print(dir(c))
print(dir(Computer))  # 'age', 'name']
c2 = Computer()
c2.name = 'c2'
print(c.name, c2.name)  # c c2
Computer.name = 'computer'  # 使用slot之后，未定义类相关属性之前，实例的属性分离，
# 定义类的相同属性之后，类，实例的属性全部为类的属性，并且该属性为ｒｅａｄ——ｏｎｌｙ
print(c2.name)
print(c.name)
print(Computer.name)


# c.name = 'cc' #AttributeError: 'Computer' object attribute 'name' is read-only

class Computer(object):
    def __init__(self):
        self.name = 'c'


print(dir(Computer))  # '__subclasshook__', '__weakref__']


class Dog(object):
    name = 'Dog'


d1 = Dog()
d1.name = 'd1'

d2 = Dog()
d2.name = 'd2'

Dog.name = 'D'

d1.name = 'dd'  # 未用slot 实例与类分开。
print(d1.name, d2.name, Dog.name)  # dd d2 D


# 第一，slots只能限制添加属性，不能限制通过添加方法来添加属性：

class Animal(object):
    __slots__ = ('name', 'age')


class Cat(Animal):
    __slots__ = ('paw')


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
c = Cat()
c.name = 'c'
c.paw = 'p'


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


s = Student()
s.score = 60
print(s.score)


# s.score=999 #ValueError: score must between 0~100!

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.width * self.height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
