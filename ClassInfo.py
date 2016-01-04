class Student(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Student object (name : %s)' % self._name

    __repr__ = __str__


print(Student('Michael'))  # Student object (name : Michael)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b

        return a


f = Fib()
print(f[0])
print(f[1])
print(f[2])

print(list(range(0, 100))[5:10])  # [5, 6, 7, 8, 9]


class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for n in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[1:5])


# __getattr__

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item == 'age':
            return lambda: 25
        raise AttributeError('Student has no attribute  %s ' % item)


s = Student()
print(s.name)
print(s.age())
# print(s.id) #AttributeError: Student has no attribute  id

class Student(object):
    def __init__(self, name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self._name)


s = Student('Michael')  # My name is Michael
s()

print(callable(Student('Michael')))  # True
print(callable(max))  # True
print(callable('str'))  # False
print(callable(None))  # False
