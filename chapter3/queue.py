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

def dance(name):
    print name + ' dancing'

def leader(name):
    global no_of_leaders
    global no_of_followers
    global leaderQueue
    global followerQueue
    followerQueue.signal()
    #The sleep is there to show the problem with the queue solution.
    #Note how all followers dance alone then leaders catch up.
    sleep(1)
    leaderQueue.wait()
    dance('leader' + name)

def follower(name):
    global no_of_leaders
    global no_of_followers
    global leaderQueue
    global followerQueue
    leaderQueue.signal()
    followerQueue.wait()
    dance('follower' + name)

[Thread(leader, str(x)) for x in xrange(no_of_leaders)]
[Thread(follower, str(x)) for x in xrange(no_of_followers)]
