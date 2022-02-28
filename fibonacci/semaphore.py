"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.

Basic example of Fibonacci sequence with Semaphore.
"""

from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print


class Fib:
    """The Fib class."""

    def __init__(self, count):
        """
        The constructor for Fib class.

        Parameter:
            count (int): The number of threads.
        """

        self.count = count
        self.counter = 0
        self.mutex = Mutex()
        self.semaphore = Semaphore(0)

    def wait(self):
        """"The Fib function with Semaphore."""

        self.mutex.lock()
        self.counter += 1
        if self.counter == self.count:
            self.semaphore.signal(self.count)
        print(self.counter)
        self.mutex.unlock()
        self.semaphore.wait()


def compute_fibonacci(fib, i):
    """The function calculates the Fibonacci sequence"""

    sleep((randint(1, 10)/10))
    fib.wait()
    fib_seq[i+2] = fib_seq[i] + fib_seq[i+1]


THREADS = 10

fib_seq = [0] * (THREADS + 2)
fib_seq[1] = 1
fib = Fib(THREADS)
threads = [Thread(compute_fibonacci, fib, i) for i in range(THREADS)]

[t.join() for t in threads]

print(fib_seq)
