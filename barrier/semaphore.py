from random import randint
from time import sleep
from fei.ppds import Thread, Semaphore, Mutex, print


class SimpleBarrier:
    def __init__(self, count):
        self.count = count
        self.counter = 0
        self.mutex = Mutex()
        self.semaphore = Semaphore(0)

    def wait(self):
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.count:
            self.counter = 0
            self.semaphore.signal(self.count)
        self.mutex.unlock()
        self.semaphore.wait()


def barrier_cycle(b1, b2, thread_id):
    while True:
        before_barrier(thread_id)
        b1.wait()
        after_barrier(thread_id)
        b2.wait()


def before_barrier(thread_id):
    sleep(randint(1, 10) / 10)
    print(f"before barrier {thread_id}")


def after_barrier(thread_id):
    print(f"after barrier {thread_id}")
    sleep(randint(1, 10) / 10)


sb1 = SimpleBarrier(5)
sb2 = SimpleBarrier(5)
thread = [Thread(barrier_cycle, sb1, sb2, i)for i in range(5)]
[t.join() for t in thread]
