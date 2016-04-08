import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0:
    print('I am a child process (%s) and my parent is %s.' % (os.getpgid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
