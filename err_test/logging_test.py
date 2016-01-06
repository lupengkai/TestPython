# logging_test.py

import logging

logging.basicConfig(level=logging.INFO)  # debug，info，warning，error

s = '0'
n = int(s)
logging.info('n = %d' % n)

# INFO:root:n = 0
