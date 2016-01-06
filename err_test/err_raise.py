# err_raise.py

class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if 0 == n:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
# Traceback (most recent call last):
#   File "/home/tage/PycharmProjects/TestPython/err_raise.py", line 13, in <module>
#     foo('0')
#   File "/home/tage/PycharmProjects/TestPython/err_raise.py", line 10, in foo
#     raise FooError('invalid value: %s' % s)
# __main__.FooError: invalid value: 0
