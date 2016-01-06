try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# try...
# except: division by zero
# finally...
# END

try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# try...
# result: 5.0
# finally...
# END

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


# try...
# ValueError: invalid literal for int() with base 10: 'a'
# finally...

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar(0)
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


main()
# Error division by zero
# finally...
