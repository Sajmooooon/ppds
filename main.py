from time import sleep
from random import randint
from fei.ppds import Thread, print, Mutex, Semaphore


class Shared(object):
    def __init__(self, number):
        self.N = number
        self.customers = 0
        self.mutex = Mutex()
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)

        self.customer_done = Semaphore(0)
        self.barber_done = Semaphore(0)


def get_hair_cut(customer_id):
    print(f"Customer {customer_id}: Getting my hair haircut.")
    sleep(1/10)


def cut_hair():
    print(f"\nBarber: Cutting hair.")
    sleep(1/10)


def balk(customer_id):
    print(f"Customer {customer_id}: The barber shop is full, "
          f"I will come next time.")
    sleep(randint(2, 3)/10)


def groving_hair(customer_id):
    print(f"Customer {customer_id}: waiting for my hair to grow.")
    sleep(randint(3, 5)/10)


def customer(customer_id, shared):
    while True:
        shared.mutex.lock()
        if shared.customers == shared.N:
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
    while True:
        shared.customer.wait()
        shared.barber.signal()
        cut_hair()
        shared.customer_done.wait()
        shared.barber_done.signal()


def main():
    capacity = 2
    customers = 3
    shared = Shared(capacity)
    threads = []
    for customer_id in range(customers):
        threads.append(Thread(customer, customer_id, shared))
    threads.append(Thread(barber, shared))
    for t in threads:
        t.join()


main()
