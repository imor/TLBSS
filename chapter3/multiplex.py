#!/usr/local/bin/python
'''
Generalize the multiplex solution so that it allows multiple threads to
run in the critical section at the same time, but it enforces an upper limit on
the number of concurrent threads. In other words, no more than n threads can
run in the critical section at the same time.
'''
from threading_cleanup import *
from time import sleep

no_of_threads_in_critical_section = 4
multiplex = Semaphore(no_of_threads_in_critical_section)
count = 0
no_of_threads = 6

def increment():
    global multiplex
    global count
    multiplex.wait()
    print count
    sleep(1)
    count = count + 1
    multiplex.signal()

[Thread(increment) for x in xrange(no_of_threads)]
