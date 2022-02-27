from fei.ppds import Thread, Mutex, print, Event


class SimpleBarrier:
    def __init__(self, count):
        self.count = count
        self.counter = 0
        self.mutex = Mutex()
        self.event = Event()

    def wait(self):
        self.mutex.lock()
        self.counter += 1
        if self.counter == self.count:
            self.counter = 0
            self.event.set()
        self.mutex.unlock()
        self.event.wait()
        self.event.clear()


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
