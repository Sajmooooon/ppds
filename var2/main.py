from collections import Counter
from fei.ppds import Thread, Mutex


class Shared:
    """This is a shared class for multiple threads"""

    def __init__(self, size):
        """
        The constructor for Shared class.

        Parameter:
        size (int): The size of array.
        """

        self.counter = 0
        self.end = size
        self.elms = [0] * size


def do_count(shared):
    """
    This function is used by threads and while loop shared array.

    Increments the value of counter
    and shared array element at position counter.
    Until counter exceeds the length of the array.

    Parameter:
    shared: The shared object.
    """

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
