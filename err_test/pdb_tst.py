# pdb_test.py

try:
    print('try...')
    r = 10 / int('a')
    print('result', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error')
finally:
    print('finally...')

# python3 -m pdb pdb_test.py

# tage@tage-PC:~/PycharmProjects/TestPython$ python3 -m pdb pdb_tst.py
# > /home/tage/PycharmProjects/TestPython/pdb_tst.py(3)<module>()
# -> try:
# (Pdb) n
# > /home/tage/PycharmProjects/TestPython/pdb_tst.py(4)<module>()
# -> print('try...')
# (Pdb) n
# try...
# > /home/tage/PycharmProjects/TestPython/pdb_tst.py(5)<module>()
# -> r = 10 / int('a')
# (Pdb) p r
# *** NameError: name 'r' is not defined
# (Pdb) q
# finally...

import pdb

pdb.set_trace()

l = 10

l = l + 1

# tage@tage-PC:~/PycharmProjects/TestPython$ python3 pdb_tst.py
# try...
# ValueError: invalid literal for int() with base 10: 'a'
# finally...
# > /home/tage/PycharmProjects/TestPython/pdb_tst.py(36)<module>()
# -> l = 10
# (Pdb) p l
# *** NameError: name 'l' is not defined
# (Pdb) n
# > /home/tage/PycharmProjects/TestPython/pdb_tst.py(38)<module>()
# -> l = l +1
# (Pdb) p l
# 10
# (Pdb) n
# --Return--
# > /home/tage/PycharmProjects/TestPython/pdb_tst.py(38)<module>()->None
# -> l = l +1
# (Pdb) p l
# 11
# (Pdb) n
