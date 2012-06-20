#!/usr/local/bin/python
'''
Add semaphores to the following example to enforce mutual exclusion
to the shared variable count.

Thread A
count = count + 1

Thread B
count = count + 1
'''

from threading_cleanup import *

mutex = Semaphore(1)
count = 0
no_of_threads = 20

def increment():
    global mutex
    global count
    mutex.wait()
    count = count + 1
    mutex.signal()
    print count

[Thread(increment) for x in xrange(no_of_threads)]
