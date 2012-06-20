#!/usr/local/bin/python
'''
Generalize the rendezvous problem to more than two threads.
Every thread should run the following code:

1 rendezvous
2 critical point
'''

from threading_cleanup import *
threads_waiting_at_rendezvous = 0
total_no_of_threads = 6
mutex = Semaphore(1)
barrier = Semaphore(0)

def func(name):
    global threads_waiting_at_rendezvous
    global total_no_of_threads
    global mutex
    global barrier

    print name + ' waiting at barrier'
    mutex.wait()
    threads_waiting_at_rendezvous += 1
    if threads_waiting_at_rendezvous == total_no_of_threads:
        barrier.signal(total_no_of_threads)
    mutex.signal()

    barrier.wait()
    print name + ' after barrier'

[Thread(func, str(x)) for x in xrange(total_no_of_threads)]
