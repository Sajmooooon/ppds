from random import randint
from time import sleep
from fei.ppds import Thread, Event, Mutex, print


class Fib:
    def __init__(self, count):
        self.count = count
        self.counter = 0
        self.mutex = Mutex()
        self.event = Event()

    def wait(self):
        self.event.clear()
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.count:
            self.event.set()
        print(self.counter)
        self.mutex.unlock()
        self.event.wait()


def compute_fibonacci(fib, i):
    sleep((randint(1, 10)/10))
    fib.wait()
    fib_seq[i+2] = fib_seq[i] + fib_seq[i+1]


THREADS = 10

fib = Fib(THREADS)
fib_seq = [0] * (THREADS + 2)
fib_seq[1] = 1

threads = [Thread(compute_fibonacci, fib, i) for i in range(THREADS)]

[t.join() for t in threads]

print(fib_seq)
