"""
  Copyright 2005 Allen B. Downey

    This file contains an example program from The Little Book of
    Semaphores, available from Green Tea Press, greenteapress.com

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see http://www.gnu.org/licenses/gpl.html
    or write to the Free Software Foundation, Inc., 51 Franklin St, 
    Fifth Floor, Boston, MA  02110-1301  USA
"""


import threading, time, os, signal, sys

class Thread(threading.Thread):
    def __init__(self, target, *args):
        threading.Thread.__init__(self, target=target, args=args)
        self.start()

class Semaphore(threading._Semaphore):
    wait = threading._Semaphore.acquire
    
    def signal(self, n=1):
        for i in range(n): self.release()

    def value(self):
        return self._Semaphore__value
    
if os.name == 'posix':
    def watcher():
        child = os.fork()
        if child == 0: return
        try:
            os.wait()
        except KeyboardInterrupt:
            print 'KeyBoardInterrupt'
            try:
                os.kill(child, signal.SIGKILL)
            except OSError:
                pass
        sys.exit()

    watcher()