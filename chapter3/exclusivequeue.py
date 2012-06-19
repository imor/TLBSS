#!/usr/local/bin/python
'''
In the queue solution it is possible for any number of leaders to dance before
any followers do. Depending on the semantics of dance, that behavior may or may
not be problematic. To make things more interesting, let's add the additional
constraint that each leader can invoke dance concurrently with only one follower,
and vice versa. In other words, you got to dance with the one that brought you.
'''

from threading_cleanup import *
from time import sleep

no_of_leaders = 4
no_of_followers = 4
leaderQueue = Semaphore(0)
followerQueue = Semaphore(0)
no_of_leaders_waiting = 0
no_of_followers_waiting = 0
mutex = Semaphore(1)
rendezvous = Semaphore(0)

def dance(name):
    print name + ' dancing'

def leader(name):
    global no_of_leaders
    global no_of_followers
    global leaderQueue
    global followerQueue
    global no_of_leaders_waiting
    global no_of_followers_waiting
    global mutex
    mutex.wait()
    if no_of_followers_waiting > 0:
        no_of_followers_waiting -= 1
        followerQueue.signal()
    else:
        no_of_leaders_waiting += 1
        mutex.signal()
        leaderQueue.wait()
    sleep(1)
    dance('leader' + name)
    rendezvous.wait()
    mutex.signal()

def follower(name):
    global no_of_leaders
    global no_of_followers
    global leaderQueue
    global followerQueue
    global no_of_leaders_waiting
    global no_of_followers_waiting
    global mutex
    mutex.wait()
    if no_of_leaders_waiting > 0:
        no_of_leaders_waiting -= 1
        leaderQueue.signal()
    else:
        no_of_followers_waiting += 1
        mutex.signal()
        followerQueue.wait()
    dance('follower' + name)
    rendezvous.signal()

[Thread(leader, str(x)) for x in xrange(no_of_leaders)]
[Thread(follower, str(x)) for x in xrange(no_of_followers)]
