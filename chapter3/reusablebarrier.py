#!/usr/local/bin/python
'''
Rewrite the barrier solution so that after all the threads have passed through,
the turnstile is locked again.
'''

from threading_cleanup import *
times_to_loop = 5
number_of_threads = 6
mutex = Semaphore(1)
number_of_threads_waiting = 0
barrier1 = Semaphore(0)
barrier2 = Semaphore(0)

def func(name):
    global times_to_loop
    global number_of_threads
    global mutex
    global number_of_threads_waiting
    global barrier1
    global barrier2

    for i in xrange(times_to_loop):
       print name + ' before barrier1'
       mutex.wait()
       number_of_threads_waiting += 1
       if number_of_threads_waiting == number_of_threads:
           barrier1.signal(number_of_threads)
       mutex.signal()

       barrier1.wait()

       print name + ' before barrier2'
       mutex.wait()
       number_of_threads_waiting -= 1
       if number_of_threads_waiting == 0:
           barrier2.signal(number_of_threads)
       mutex.signal()

       barrier2.wait()

[Thread(func, str(x)) for x in xrange(number_of_threads)]
