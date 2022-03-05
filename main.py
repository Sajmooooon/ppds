from random import randint
from time import sleep
from fei.ppds import Mutex, Semaphore, Thread, print


class LightSwitch(object):
    def __init__(self):
        self.cnt = 0
        self.mutex = Mutex()

    def lock(self, sem):
        self.mutex.lock()
        if not sem.cnt:
            sem.wait()
        self.cnt += 1
        self.mutex.unlock()

    def unlock(self, sem):
        self.mutex.lock()
        self.cnt -= 1
        if not sem.cnt:
            sem.signal()
        self.mutex.unlock()


class Shared(object):
    def __init__(self, count):
        self.finished = False
        self.mutex = Mutex()
        self.free = Semaphore(count)
        self.items = Semaphore(0)


def producer(shared):
    while True:
        sleep(randint(1, 10)/10)
        shared.free.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        sleep(randint(1, 10) / 100)
        shared.mutex.unlock()
        shared.items.signal()


def consumer(shared):
    while True:
        shared.items.wait()
        if shared.finished:
            break
        shared.mutex.lock()
        sleep(randint(1, 10) / 100)
        shared.mutex.unlock()
        sleep(randint(1, 10) / 10)


def main():
    for i in range(10):
        s = Shared(10)
        c = [Thread(consumer, s) for _ in range(2)]
        p = [Thread(producer, s) for _ in range(5)]

        sleep(5)
        s.finished = True
        print(f"main thread {i}: awaiting completion")
        s.items.signal(100)
        s.free.signal(100)
        [t.join() for t in c+p]
        print(f"main thread {i}: end of program")


main()
