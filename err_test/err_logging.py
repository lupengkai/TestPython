# err_logging.py

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')


main()
print('END')

# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "/home/tage/PycharmProjects/TestPython/err_logging.py", line 13, in main
#     bar(0)
#   File "/home/tage/PycharmProjects/TestPython/err_logging.py", line 9, in bar
#     return foo(s) * 2
#   File "/home/tage/PycharmProjects/TestPython/err_logging.py", line 6, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# finally...
# END
