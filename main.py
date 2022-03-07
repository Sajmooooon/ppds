"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.

Implementation of the Consumer-Producer problem.
"""

import matplotlib.pyplot as plt
from random import randint
from time import sleep
from fei.ppds import Mutex, Semaphore, Thread, print


class Shared(object):
    """This is a shared class for multiple threads"""

    def __init__(self, count):
        """
        The constructor for Shared class.

        Parameter:
        count (int): The size of warehouse.
        """

        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(count)
        self.items = Semaphore(0)
        self.counter = 0


def producer(shared, time):
    """
    The function of producer.

    Parameters:
        shared (object): The shared object.
        time (float): The time of item production.
    """

    while True:
        sleep(time)
        shared.free.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        sleep(randint(1, 10) / 400)
        shared.counter += 1
        shared.mutex.unlock()
        shared.items.signal()


def consumer(shared):
    """
    The function for consumer.

    Parameters:
        shared (object): The shared object.
    """

    while True:
        shared.items.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        sleep(randint(1, 10) / 400)
        shared.mutex.unlock()
        sleep(randint(1, 10) / 250)


def grid_search():
    """The function for grid search."""

    output = []
    for produce_time in range(10):
        for count_consumers in range(1, 11):
            sum_item = 0
            for i in range(10):
                s = Shared(10)
                time = (produce_time + 1) / 250
                c = [Thread(consumer, s) for _ in range(count_consumers)]
                p = [Thread(producer, s, time) for _ in range(10)]

                sleep(0.05)
                s.finished = True
                print(f"main thread {i}: awaiting completion")
                s.items.signal(100)
                s.free.signal(100)
                [t.join() for t in c + p]
                print(f"main thread {i}: end of program")
                items = s.counter / time
                sum_item += items

            avr_items = sum_item / 10
            output.append((time, count_consumers, avr_items))
    return output


def show(output):
    """
    The function to show figure.

    Parameters:
        output (list): The list of data from grid search.
    """

    plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('Production time')
    ax.set_ylabel('Number of consumers')
    ax.set_zlabel('Number of products')
    x = [time[0] for time in output]
    y = [consumer[1] for consumer in output]
    z = [size[2] for size in output]
    ax.plot_trisurf(x, y, z, cmap='plasma', edgecolor='none')
    ax.set_title('Number of products produced per unit time')
    plt.show()


output = grid_search()
show(output)
