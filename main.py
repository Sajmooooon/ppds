from time import sleep
from random import randint
from fei.ppds import Thread, print, Mutex, Semaphore


class SimpleBarrier(object):
    def __init__(self, number):
        self.number = number
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
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
    def __init__(self, servings):
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
    print(f'🐗 savage {savage_id}: eating')
    sleep(randint(50, 200) / 100)


def savage(savage_id, shared):
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
