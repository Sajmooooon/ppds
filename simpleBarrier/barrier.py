"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.

Basic example of synchronization pattern Semaphore.
"""

from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print


class SimpleBarrier:
    """The SimpleBarrier class."""

    def __init__(self, count):
        """
        The constructor for SimpleBarrier class.

        Parameter:
            count (int): The number of threads.
        """

        self.count = count
        self.counter = 0
        self.mutex = Mutex()
        self.semaphore = Semaphore(0)

    def wait(self):
        """"The SimpleBarrier function with Semaphore."""

        self.mutex.lock()
        self.counter += 1
        if self.counter == self.count:
            self.counter = 0
            self.semaphore.signal(self.count)
        self.mutex.unlock()
        self.semaphore.wait()


def barrier_cycle(barrier, thread_id):
    """"
    The function prints threads id before and after barrier.

    Parameters:
        barrier (obj): The SimpleBarrier object.
        thread_id (int): The id of thread.
    """

    sleep(randint(1, 10) / 10)
    print(f"before barrier {thread_id}")
    barrier.wait()
    print(f"after barrier {thread_id}")


sb1 = SimpleBarrier(5)
thread = [Thread(barrier_cycle, sb1, i)for i in range(5)]
[t.join() for t in thread]
