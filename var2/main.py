from collections import Counter
from fei.ppds import Thread, Mutex


class Shared:
    def __init__(self, size):
        self.counter = 0
        self.end = size
        self.elms = [0] * size


def do_count(shared):
    while True:
        mutex.lock()
        if shared.counter >= shared.end:
            mutex.unlock()
            break
        shared.elms[shared.counter] += 1
        shared.counter += 1
        mutex.unlock()


mutex = Mutex()

shared = Shared(1_000_000)
t1 = Thread(do_count, shared)
t2 = Thread(do_count, shared)
t1.join()
t2.join()

counter = Counter(shared.elms)
print(counter.most_common())
