"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.

Basic example of synchronization pattern Event.
"""

from random import randint
from time import sleep
from fei.ppds import Thread, Mutex, print, Event


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
        self.event = Event()

    def wait(self):
        """"The SimpleBarrier function with Event."""

        self.mutex.lock()
        self.counter += 1
        if self.counter == self.count:
            self.counter = 0
            self.event.set()
        self.mutex.unlock()
        self.event.wait()
        self.event.clear()


def barrier_cycle(b1, b2, thread_id):
    """"
    The function while loop 2 barriers in endless loop.

    Parameters:
        b1 (obj): First SimpleBarrier object.
        b2 (obj): Second SimpleBarrier object.
        thread_id (int): The id of thread.
    """

    while True:
        before_barrier(thread_id)
        b1.wait()
        after_barrier(thread_id)
        b2.wait()


def before_barrier(thread_id):
    """"
    The function print thread id for thread before barrier.

    Parameter:
        thread_id (int): The id of thread.
    """

    sleep(randint(1, 10) / 10)
    print(f"before barrier {thread_id}")


def after_barrier(thread_id):
    """"
    The function print thread id for thread after barrier.

    Parameter:
        thread_id (int): The id of thread.
    """

    print(f"after barrier {thread_id}")
    sleep(randint(1, 10) / 10)


sb1 = SimpleBarrier(5)
sb2 = SimpleBarrier(5)
thread = [Thread(barrier_cycle, sb1, sb2, i)for i in range(5)]
[t.join() for t in thread]
