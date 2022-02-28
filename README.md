# PPDS 02
Second assignment from the PPDS course.


## Description
In this assignment, we were concerned with solving 3 problems using a semaphore and an event.
In the first problem we created a simple barrier.
In the second problem we solved a reusable barrier and in the third problem we solved a fibonacci.
The implementation of the simple barrier is located at [simple barrier](https://github.com/Sajmooooon/ppds/tree/02/simpleBarrier) with the reusable barrier located at [reusable barrier](https://github.com/Sajmooooon/ppds/tree/02/barrier)
folder and the fibonacci implementation is located in the fibonacci folder.


## ADT Simple Barrier
In this task, we created a simple barrier using a semaphore, where the ids of the threads before and after the barrier were printed out.
The barrier is provided by the ``wait()`` function in the ``SimpleBarrier``  class. In this function, the
thread is locked, then the counter is incremented, which is then
checks that its value is the same as the thread count. If so, the counter is reset. Next 
all threads are released, the thread is unlocked, and finally the thread is waited for to catch up if the condition has been met,
then all waiting threads are released.

