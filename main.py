from time import sleep
from random import randint
from fei.ppds import Thread, print, Mutex, Semaphore


class SimpleBarrier(object):
    def __init__(self, N):
        self.N = N
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
        self.mutex.lock()
        self.count += 1
        if each:
            print(each)
        if self.count == self.N:
            if last:
                print(last)
            self.count = 0
            self.barrier.signal(self.N)
        self.mutex.unlock()
        self.barrier.wait()


class Shared(object):
    def __init__(self, m):
        self.servings = m
        self.mutex = Mutex()
        self.empty_pot = Semaphore(0)
        self.full_pot = Semaphore(0)

        self.b1 = SimpleBarrier(N)
        self.b2 = SimpleBarrier(N)


def eat(i):
    print(f'🐗 savage {i}: eating')
    sleep(randint(50, 200) / 100)


def savage(i, shared):
    sleep(randint(1, 100)/100)
    while True:
        shared.b1.wait()
        shared.b2.wait(each=f'🐗 savage {i}: before dinner',
                       last=f'🐗 savage {i}: we are all')
        shared.mutex.lock()
        print(f'🐗 savage {i}: number of remaining portions {shared.servings}')
        if shared.servings == 0:
            print(f'🐗 savage {i}: wake the cook')
            shared.empty_pot.signal()
            shared.full_pot.wait()
        print(f'🐗 savage {i}: taking from pot')
        shared.servings -= 1
        shared.mutex.unlock()
        eat(i)


def cook(shared):
    while True:
        shared.empty_pot.wait()
        print('‍🍳 cook: cooking')
        sleep(randint(50, 200)/100)
        shared.servings += M
        shared.full_pot.signal()


def main():
    shared = Shared(0)
    savages = []
    for i in range(N):
        savages.append(Thread(savage, i, shared))
    savages.append(Thread(cook, shared))


N = 3
M = 20
main()
