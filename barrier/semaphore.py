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
        print(f"before barrier {thread_id}")
        b1.wait()
        print(f"after barrier {thread_id}")
        b2.wait()


sb1 = SimpleBarrier(5)
sb2 = SimpleBarrier(5)
thread = [Thread(barrier_cycle, sb1, sb2, i)for i in range(5)]
[t.join() for t in thread]
