# err_assert.py

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


foo(0)

# Traceback (most recent call last):
#   File "/home/tage/PycharmProjects/TestPython/err_assert.py", line 8, in <module>
#     foo(0)
#   File "/home/tage/PycharmProjects/TestPython/err_assert.py", line 5, in foo
#     assert n != 0, 'n is zero'
# AssertionError: n is zero
