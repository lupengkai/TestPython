try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error')
# Traceback (most recent call last):
#   File "/home/tage/PycharmProjects/TestPython/err_convert.py", line 2, in <module>
#     10 / 0
# ZeroDivisionError: division by zero
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "/home/tage/PycharmProjects/TestPython/err_convert.py", line 4, in <module>
#     raise ValueError('input error')
# ValueError: input error
