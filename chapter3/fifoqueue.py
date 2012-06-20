#!/usr/local/bin/python
'''
Use semaphores to build a first-in-first-out queue. Each time the Fifo
is signaled, the thread at the head of the queue should proceed. If more than
one thread is waiting on a semaphore, you should not make any assumptions
about which thread will proceed when the semaphore is signaled.

For bonus points, your solution should define a class named Fifo that
provides methods named wait and signal
'''

from threading_cleanup import *
from Queue import Queue
from random import randrange
from time import sleep

class Fifo:
    def __init__(self):
        self.queue = Queue()
        self.mutex = Semaphore(1)

    def wait(self):
        sem = Semaphore(0)
        self.mutex.wait()
        self.queue.put(sem)
        self.mutex.signal()
        sem.wait()

    def signal(self):
        self.mutex.wait()
        sem = self.queue.get()
        self.mutex.signal()
        sem.signal()

fifo = Fifo()

def wait(name):
    #sleep(randrange(1, 3))
    print 'Thread' + name + ' waits'
    fifo.wait()
    print 'Thread' + name + ' goes'

def signal():
    fifo.signal()

Thread(wait, '0')
sleep(1)
Thread(wait, '1')
sleep(1)
Thread(wait, '2')
sleep(1)
Thread(wait, '3')
sleep(1)
Thread(wait, '4')
sleep(5)
Thread(signal)
sleep(1)
Thread(signal)
sleep(1)
Thread(signal)
sleep(1)
Thread(signal)
sleep(1)
Thread(signal)


#Please note that this solution is not perfect. If the above Fifo class is
#signaled before it is waited on, the waiting thread is never unblocked this
#is different from the semantics of a Semaphore. Still looking for a better
#solution
