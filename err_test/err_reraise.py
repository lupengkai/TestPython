# err_reraise.py

def foo(s):
    n = int(s)
    if 0 == n:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo(0)

    except ValueError as e:
        print('ValueError!')
        raise


bar()

# Traceback (most recent call last):
#   File "/home/tage/PycharmProjects/TestPython/err_reraise.py", line 18, in <module>
#     bar()
#   File "/home/tage/PycharmProjects/TestPython/err_reraise.py", line 12, in bar
#     foo(0)
#   File "/home/tage/PycharmProjects/TestPython/err_reraise.py", line 6, in foo
#     raise ValueError('invalid value: %s' % s)
# ValueError: invalid value: 0
