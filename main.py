"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.
Implementation of the problem of barber and multiple customers.
"""


from time import sleep
from random import randint
from fei.ppds import Thread, print, Mutex, Semaphore


class Shared(object):
    """This is a shared class for multiple threads."""

    def __init__(self, number):
        """
        The constructor for Shared class.

        Parameter:
        number (int): The capacity of barber shop.
        """

        self.shop_capacity = number
        self.customers = 0
        self.mutex = Mutex()
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)

        self.customer_done = Semaphore(0)
        self.barber_done = Semaphore(0)


def get_hair_cut(customer_id):
    """"
    The simple function to simulate getting haircut.

    Parameter:
        customer_id (int): The ID of customer.
    """

    print(f"Customer {customer_id}: Getting my hair haircut.")
    sleep(1/10)


def cut_hair():
    """"The simple function to simulate cutting hair."""

    print(f"\nBarber: Cutting hair.")
    sleep(1/10)


def balk(customer_id):
    """"
    The simple function to simulate leaving from barber shop because is full.

    Parameter:
        customer_id (int): The ID of customer.
    """

    print(f"Customer {customer_id}: The barber shop is full, "
          f"I will come next time.")
    sleep(randint(2, 3)/10)


def groving_hair(customer_id):
    """"
    The simple function to simulate waiting for hair growth.

    Parameter:
        customer_id (int): The ID of customer.
    """

    print(f"Customer {customer_id}: waiting for my hair to grow.")
    sleep(randint(3, 5)/10)


def customer(customer_id, shared):
    """
    The function simulates the customer at the barber shop.

    Parameters:
        customer_id (int): The ID of customer.
        shared (object): The shared object.
    """

    while True:
        shared.mutex.lock()
        if shared.customers == shared.shop_capacity:
            shared.mutex.unlock()
            balk(customer_id)
        else:
            shared.customers += 1
            print(f"Customer {customer_id}: Waiting for cuting.")
            shared.mutex.unlock()

            shared.customer.signal()
            shared.barber.wait()

            get_hair_cut(customer_id)
            shared.customer_done.signal()
            shared.barber_done.wait()

            shared.mutex.lock()
            shared.customers -= 1
            shared.mutex.unlock()
            groving_hair(customer_id)


def barber(shared):
    """
    The function simulates hair cutting by barber.

    Parameters:
        shared (object): The shared object.
    """

    while True:
        shared.customer.wait()
        shared.barber.signal()
        cut_hair()
        shared.customer_done.wait()
        shared.barber_done.signal()


def main():
    """This function is for program initialization."""

    capacity = 3
    customers = 6
    shared = Shared(capacity)
    threads = []
    for customer_id in range(customers):
        threads.append(Thread(customer, customer_id, shared))
    threads.append(Thread(barber, shared))
    for t in threads:
        t.join()


main()
