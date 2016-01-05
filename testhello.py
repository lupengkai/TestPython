from hello import Hello

h = Hello()
h.hello()
print(type(Hello))  # <class 'type'>
print(type(h))  # <class 'hello.Hello'>


def fn(self, name='world'):
    print('Hello %s', name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print(type(Hello))  # <class 'type'>
print(type(h))  # <class '__main__.Hello'>


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)
