"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.
Implementation of the problem of Savages and Cooks.
"""

from time import sleep
from random import randint
from fei.ppds import Thread, print, Mutex, Semaphore


class SimpleBarrier(object):
    """"The SimpleBarrier class."""

    def __init__(self, number):
        """
        The constructor for SimpleBarrier class.

        Parameter:
            number (int): The number of threads.
        """
        self.number = number
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
        """"The SimpleBarrier function with Semaphore."""

        self.mutex.lock()
        self.count += 1
        if each:
            print(each)
        if self.count == self.number:
            if last:
                print(last)
            self.count = 0
            self.barrier.signal(self.number)
        self.mutex.unlock()
        self.barrier.wait()


class Shared(object):
    """This is a shared class for multiple threads."""

    def __init__(self, servings):
        """
        The constructor for Shared class.

        Parameter:
        servings (int): The number of servings.
        """

        self.servings = servings
        self.count = 0
        self.mutex = Mutex()
        self.cmutext = Mutex()
        self.empty_pot = Semaphore(0)
        self.full_pot = Semaphore(0)

        self.b1 = SimpleBarrier(number_savages)
        self.b2 = SimpleBarrier(number_savages)

        self.c1 = SimpleBarrier(number_cooks)
        self.c2 = SimpleBarrier(number_cooks)


def eat(savage_id):
    """"
    The simple function to simulate eating.

    Parameter:
        savage_id (int): The ID of savage.
    """

    print(f'🐗 savage {savage_id}: eating')
    sleep(randint(50, 200) / 100)


def savage(savage_id, shared):
    """
    The function simulates waiting for others savages and start eating and
    notifing cooks when pot is empty.

    Parameters:
        savage_id (int): The ID of savage.
        shared (object): The shared object.
    """

    sleep(randint(1, 100)/100)
    while True:
        shared.b1.wait()
        shared.b2.wait(each=f'🐗 savage {savage_id}: before dinner',
                       last=f'🐗 savage {savage_id}: we are all')
        shared.mutex.lock()
        print(f'🐗 savage {savage_id}: number of remaining portions {shared.servings}')
        if shared.servings == 0:
            print(f'🐗 savage {savage_id}: wake the cook')
            shared.empty_pot.signal(number_cooks)
            shared.full_pot.wait()
        print(f'🐗 savage {savage_id}: taking from pot')
        shared.servings -= 1
        shared.mutex.unlock()
        eat(savage_id)


def cook(cook_id, shared):
    """
   The function simulates waiting for others cooks and start cooking,
   then notifing savage when pot is full.

   Parameters:
       cook_id (int): The ID of cook.
       shared (object): The shared object.
   """

    while True:
        shared.c1.wait()
        shared.c2.wait()
        shared.empty_pot.wait()
        shared.cmutext.lock()
        shared.count += 1
        print(f'‍🍳 cook {cook_id}: cooking')
        if shared.count == number_cooks:
            sleep(randint(50, 200) / 100)
            shared.count = 0
            print(f'🍳 cook {cook_id}: servings -> pot')
            shared.servings += number_servings
            shared.full_pot.signal()
        shared.cmutext.unlock()


def main():
    """This function is for program initialization."""

    shared = Shared(0)
    threads = []
    for savage_id in range(number_savages):
        threads.append(Thread(savage, savage_id, shared))
    for cook_id in range(number_cooks):
        threads.append(Thread(cook, cook_id, shared))
    for t in threads:
        t.join()


number_savages = 3
number_cooks = 5
number_servings = 10
main()
